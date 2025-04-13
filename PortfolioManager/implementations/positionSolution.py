import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.positionInterface import positionInterface
from interfaces.securityInterface import securityInterface
from implementations.securitySolution import security as sec

class position(positionInterface):

    def __init__(self, security: str | sec, initialPosition: int) -> None:
        if isinstance(security, str):
            self.security = sec(security)
        else:
            self.security: sec = security
        self.initialPosition: int = initialPosition

    def __str__(self):
        return f"{str(self.security)}, {self.initialPosition}"

    def getSecurity(self) -> sec:
        return self.security

    def getPosition(self) -> int:
        return self.initialPosition
    
    def setPosition(self, inputValue: int) -> None:
        if inputValue <= 0:
            raise Exception("Negative position")
        self.initialPosition = inputValue
    
    def addPosition(self, inputValue: int) -> None:
        if self.initialPosition + inputValue <= 0:
            raise Exception("Negative position")
        self.initialPosition = self.initialPosition + inputValue

    def getCurrentMarketValue(self) -> float:
        return self.security.getCurrentMarketValue() * self.initialPosition
