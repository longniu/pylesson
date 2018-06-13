# Import module ex_module
from ex_module import Datalog

# Defined a sub class of super class :Datalog
class Mydata(Datalog):
    def printlog(self):
        for date, data in self.loglist:
            print(date, data)
