class Binarytree:
    def __init__(self,gen):
        self.gen=gen
        self.lefttree=None
        self.righttree=None

    def insertlefttree(self,newleft):
        if self.lefttree==None:
            self.lefttree=newleft

        else:
            t=Binarytree(newleft)
            t.lefttree=self.lefttree
            self.lefttree=t

    def insertrighttree(self,newright):
        if self.righttree==None:
            self.righttree=newright

        else:
            t=Binarytree(newright)
            t.righttree=self.righttree
            self.righttree=t

    def getlefttree(self):
        return self.lefttree

    def getrighttree(self):
        return self.righttree

    def getgen(self):
        return self.gen

    def setgen(self,obj):
        self.gen=obj


a=Binarytree('a')
print(a.getgen())
a.insertlefttree('b')
print(a.getlefttree())