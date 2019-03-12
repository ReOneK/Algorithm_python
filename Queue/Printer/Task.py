import random


class Task:
    def __init__(self,time):
        self.timetamp=time
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timetamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime-self.timetamp


