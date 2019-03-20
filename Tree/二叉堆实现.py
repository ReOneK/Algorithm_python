"""使用列表构建二叉堆"""
class binaryheap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0

    def add_up(self,i):
        a=self.currentsize//2
        while a>0:
            if self.heaplist[i]<self.heaplist[a]:
                temp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[a]
                self.heaplist[a]=temp

            a=self.currentsize//2

    def insert(self,i):
        self.heaplist.append(i)
        self.currentsize+=1
        self.add_up(self.currentsize)

    def findminchild(self,i):
        if self.heaplist[i*2+1]>self.heaplist[self.currentsize]:
            return 2*i
        else:
            if self.heaplist[i*2]<self.heaplist[2*i+1]:
                return 2*i+1
            else:
                return 2*i

    def del_dowm(self,i):
        while i*2<=self.currentsize:
            minchild=self.findminchild(i)
            if self.heaplist[i]>self.heaplist[minchild]:
                temp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[minchild]
                self.heaplist[minchild]=temp
            i=minchild

    def min(self):
        topvalue=self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize-=1
        self.heaplist.pop()
        self.del_dowm(1)


    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        while (i > 0):
            self.del_dowm(i)
            i = i - 1

bh = binaryheap()
bh.buildHeap([9,5,6,2,3])
print(bh.insert(4))
