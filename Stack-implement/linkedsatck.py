"""
用python实现简易的链表栈
使用头插法
"""

from node import Node


class Linkedstack(object):
    def __init__(self,collection=None):
        self._size=0
        self._items=None

    def __iter__(self):
        def visitnode(node):
            if node is not None:
                visitnode(node.next)
                templist.append(node.data)
        templist=list()
        visitnode(self._items)
        return iter(templist)

    def isempty(self):
        return len(self) == 0

    def peek(self):
        if self.isempty():
            raise KeyError("list is blank")
        return self._items.data

    def claer(self):
        self._size = 0
        self._items = None

    def push(self,item):
        self._items = Node(item,self._size)
        self._size += 1

    def pop(self):
        if self.isempty():
            raise KeyError("is empty")
        olditem = self._items.data
        self._items = self._items.next
        self._size -= 1
        return olditem

