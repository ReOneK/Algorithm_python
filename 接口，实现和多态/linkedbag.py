from node import  Node


class Linkedbag(object):
    """
    基于链表的实现
    """

    def __init__(self, collection=None):
        self._items = Node
        self._size = 0
        if collection:
            for item in collection:
                self.add(item)

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def add(self,item):
        self._items=Node(item,self._items)
        self._size += 1

    def remove(self,item):
        probe = self._items   #prob为头节点
        trailer = None        #trailer为prob的下一个节点
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        #若查询的节点位于头部的节点，则
        if probe == self._items:
            self._items = self._items.next
        #若不是头节点
        else:
            trailer.next = probe.next

        self._size -= 1
