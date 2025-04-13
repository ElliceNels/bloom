import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from copy import copy
from typing import Set, Iterable
from interfaces.accountInterface import accountInterface
from interfaces.portfolioInterface import portfolioInterface
from interfaces.securityInterface import securityInterface 

class portfolio(portfolioInterface):
    def __init__(self, portfolioName: str, accounts: Set[accountInterface] = set()) -> None:
        self.portfolioName: str = portfolioName
        self.accounts: Set = set(copy(accounts))

    def __str__(self) -> str:
        st = ""
        for a in self.accounts:
            st += "\n" + str(a)
        print("INCLASS", f"Portfolio Name:{self.portfolioName}\nAccounts:{st}")
        return f"Portfolio Name:{self.portfolioName}\nAccounts:{st}"

    def getPortfolioName(self) -> str:
        return self.portfolioName

    def getAllAccounts(self) -> Iterable[accountInterface]:
        return self.accounts

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        nameValidAcc = [acc for acc in self.accounts if acc.getName() in accountNamesFilter]
        secValidAcc = [acc for acc in nameValidAcc if acc.getPositions(securitiesFilter)]
        
        return secValidAcc

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        existingAccNames = {a.getName(): a for a in self.accounts}
        for acc in accounts:
            if acc.getName() in existingAccNames:
                self.accounts.remove(existingAccNames[acc.getName()])
            self.accounts.add(acc)

    def removeAccounts(self, accountNames: Set[str]) -> None:
        new_accounts = copy(self.accounts)
        for acc in new_accounts:
            if acc.getName() in accountNames:
                self.accounts.remove(acc)

    def removeAllAccounts(self) -> None:
        self.accounts.clear()

    def getCurrentMarketValue(self) -> dict:
        values = {}
        for acc in self.accounts:
            values[acc.getName()] = acc.getCurrentMarketValue()
        return values

    def getCurrentFilteredMarketValue(self, securities: Set, accountNames: Set[str]) -> float:
        totalMV = 0
        validSecAcc = [acc for acc in self.accounts if acc.getPositions(securities)]
        validAcc = [acc for acc in validSecAcc if acc.getName() in accountNames]    
            
        for acc in validAcc:
            totalMV += acc.getCurrentMarketValue() 

        return totalMV
