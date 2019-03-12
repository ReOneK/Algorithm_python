from Node import Node


class unorderNode:
    def __init__(self):
        self.head=None

    def add(self,item):
        temp=Node(item)
        temp.setnext(self.head)
        self.head=temp

    def isEmpty(self):
        return self.head == None

    def size(self):
        index=0
        current=self.head
        while current != None:
            index+=1
            current=current.getnext()
        return index

    def research(self,item):
        current=self.head
        while current != None:
            if current.getdata()==item:
                return True
            else:
                return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()

        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())
