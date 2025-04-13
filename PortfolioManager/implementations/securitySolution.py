#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from generators.priceDataGenerator import priceData
from interfaces.securityInterface import securityInterface 

class security(securityInterface):
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return self.name

    def getName(self) -> str:
        return self.name

    def getCurrentMarketValue(self) -> float:
        return priceData().getCurrentPrice(self.name)