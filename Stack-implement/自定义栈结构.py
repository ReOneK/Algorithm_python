class Stack:
     """
     自定义栈结构

     """
     def __init__(self):
          self.items=[]


     def isEmpty(self):
          return self.items==[]


     def push(self,item):
          self.items.push(item)


     def pop(self):
          self.items.pop()


     def peek(self):
          return slef.items[len(self.items)-1]

     def size(self):
          return len(self.items)
