"""
使用头插法实现数组栈
"""



from arrays import Array


class ArrayStack:
    capacity = 10

    def __init__(self,collection=None):
        self._item = Array(ArrayStack.capacity)
        self._size = 0

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._item[cursor]
            cursor += 1

    def peek(self):
        return self._item[len(self)-1]

    def push(self,item):
        self._item[len(self)] = item
        self._size += 1

    def pop(self):
        olditem = self._item[len(self)-1]
        self._size -= 1
        return olditem
