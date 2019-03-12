"""
队列模拟：烫手山芋

"""

from pythonds.basic.queue import Queue


def game(names,num):
     q=Queue()
     
     for i in names:
          q.enqueue(i)

     while q.size()>1:
          for i in range(num):
               q.enqueue(q.dequeue())
          q.dequeue()

     return q.dequeue()


print(game(["Bill","David","Susan","Jane","Kent","Brad"],7))
