class Array(object):
    def __init__(self, capacity, fileValue=None):
        self._items = []
        for i in range(capacity):
            self._items.append(fileValue)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, newvalue):
        self._items[index] = newvalue

