"""
使用python实现简单的后缀表达式
"""


class Stack(object):
    """
    这里是基于列表的栈（将列表作为基础数据结构）
    push 往里面放
    peek 查看栈顶元素
    pop 弹出栈顶元素，并返回这个方法的返回值
    empty 判断栈是否为空
    """

    def __init__(self):
        self.datas = []
        self.length = 0

    def push(self,data):
        self.datas.append(data)
        self.length += 1

    def peek(self):
        return None if self.empty() else self.datas[len(self.datas) - 1]

    def pop(self):
        try:
            return self.peek()
        finally:
            self.length -= 1
            del self.datas[len(self.datas) - 1]

    def empty(self):
        return not bool(self.length)

    def __str__(self):
        return ','.join([str(data) for data in self.datas])

