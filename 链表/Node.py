class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def getdata(self):
        return self.data

    def setdata(self,newdata):
        self.data=newdata

    def getnext(self):
        return self.next

    def setnext(self,newnext):
        self.next=newnext
temp=Node(23)
print(temp.getdata())
