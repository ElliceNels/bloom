import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from typing import Set, Iterable, Dict, Any, Optional
from interfaces.accountInterface import accountInterface
from interfaces.positionInterface import positionInterface
from copy import copy

class account(accountInterface):

    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.accountName = accountName
        if not positions:
            positions = set()
        self.positions = set(copy(positions))

    def __str__(self):
        st = ""
        for p in self.positions:
            st += "\n" + str(p)
        return f"Account Name:{self.accountName}\nPositions:{st}"

    def getName(self) -> str:
        return self.accountName

    def getAllPositions(self) -> Iterable[positionInterface]:
        return self.positions

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        correspPoses = [
            pos 
            for pos in self.positions 
            if str(pos.getSecurity()) in [str(security) for security in securities]
        ]
        actualRes = {
            sec: p 
            for p in correspPoses
            for sec in securities 
            if str(p.getSecurity()) == str(sec)
        }
        return actualRes

    def addPositions(self, positions: Set[positionInterface]) -> None:
        existingPosSecNames = {p.getSecurity().getName(): p for p in self.positions}
        for pos in positions:
            if pos.getSecurity().getName() in existingPosSecNames:
                self.positions.remove(existingPosSecNames[pos.getSecurity().getName()])
            self.positions.add(pos)
    
    def removePositions(self, securities: Set) -> None:
        self.positions = [validPos for validPos in self.positions if str(validPos.getSecurity()) not in [str(security) for security in securities]]

    def removeAllPositions(self) -> None:
        self.positions.clear()

    def getCurrentMarketValue(self) -> float:
        totalMV: float = 0
        for pos in self.positions:
            totalMV += pos.getCurrentMarketValue()
        return totalMV

    def getCurrentFilteredMarketValue(self, securities: Set) -> float:
        filteredMV: float = 0
        for pos in self.getPositions(securities).values():
            filteredMV += pos.getCurrentMarketValue()
        return filteredMV
