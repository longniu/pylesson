# datetime module
from datetime import datetime

# define Datalog Class
class Datalog:
    # constractor
    def __init__(self):
        self.loglist = []

    # Instance method
    def log(self, data):
        now = datetime.now()
        item = (now, data)
        self.loglist.append(item)
