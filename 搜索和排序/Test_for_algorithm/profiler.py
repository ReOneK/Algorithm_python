"""
简要介绍算法
"""
import random
import time


class Profiler(object):
    def __init__(self):
        print("start\n")

    def test(self, functionl, lst=None, size =10, unique=True, comp=True, exch=True, trace=True):
        """
        测试算法的功能
        :param function: 算法文件
        :param lst: 测试列表
        :param size: 列表大小
        :param unique: 如果为真，随机生成列表项
        :param comp: 如果为真，显示交换结果
        :param exch: 是否交换
        :param trace: 打印交换后的结果
        :return: 交换后的数组
        """
        self._comp=comp
        self._exch=exch
        self._trace=trace

        if lst!=None:
            self._lst=lst

        elif unique:
            self._lst = list(range(1, size+1))
            random.shuffle(self._lst)

        else:
            self._lst = []
            for count in range(size):
                self._lst.append(random.randint(1,size))

        self._exchcount = 0
        self._cmpcount = 0
        self.startclock()
        functionl(self._lst,self)
        self.stopclock()
        self.show()

    def exchange(self):
        if self._exch:
            self._exchcount += 1
        if self._trace:
            print(self._lst)

    def comparison(self):
        if self._comp:
            self._cmpcount += 1

    def startclock(self):
        self.start = time.time()

    def stopclock(self):
        self.stop = time.time()-self.start

    def show(self):
        result = "Problem size:"
        result += str(len(self._lst)) + "\n"

        if self._comp:
            result += "Comparision:"
            result += str(self._cmpcount) + "\n"
        print(result)
        if self._exch:
            result = "Exchange:"
            result += str(self._exchcount) + "\n"
        print(result)

    def __str__(self):
        result = "Problem size:"
        result += str(len(self._lst)) + "\n"

        result += "stop time:"
        result += str(self.stopclock())+"\n"
        print(result)
        if self._comp:
            result += "Comparision:"
            result += str(self._cmpcount)+"\n"

        if self._exch:
            result = "Exchange:"
            result += str(self._exchcount)+"\n"

        return result

