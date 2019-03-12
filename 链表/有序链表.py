from Node import Node


class unorderNode:
    def __init__(self):
        self.head=None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setnext(self.head)
            self.head = temp
        else:
            temp.setnext(current)
            previous.setnext(temp)

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
        stop=False
        not_exist=False
        while current != None and not stop and not not_exist:
            if current.getdata()==item:
                stop=True
            elif current.getdata>item:
                not_exist=True
            else:
                current.getnext()
        return stop

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
