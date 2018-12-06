from arrays import Array


class Arraybag(object):
    """
    开发一个基于接口的实现
    """
    capacity = 10

    def __init__(self,collection=None):
        self._items = Array(Arraybag.capacity)
        self._size = 0
        if collection:
            for item in collection:
                self.add(item)

    def isempty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._items = Array(Arraybag.capacity)

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __iter__(self):
        cursor=0
        while cursor<len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        return "{" + ", ".join(map(str,self)) + "}"

    def __add__(self, other):
        result = Arraybag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True

        if type(self)!=type(other) or len(self)!=len(other):
            return False

        for item in self:
            if not item in other:
                return False
            return True

    def remove(self,item):
        if not item in self:
            raise KeyError(str(item)+"not in bag")

        targetindex=0
        for targetitem in self:
            if targetitem==item:
                break
            targetindex += 1

        for i in range(targetindex,len(self)-1):
            self._items[i]=self._items[i+1]

        self._size -= 1

