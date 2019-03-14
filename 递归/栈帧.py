"""
Python 如何实现一个递归函数调用。 当在 Python 中调用函数时，会
分配一个栈来处理函数的局部变量。当函数返回时，返回值留在栈的顶部，以供调用函数访问。
"""
from pythonds.basic.stack import Stack


def demo(n,base):
    s=Stack()
    all_string='0123456789ABCDEF'
    while n>0:
        if n<base:
            s.push(all_string[n])
        else:
            s.push(all_string[n%base])
        n=n//base

    str=''
    while not s.isEmpty():
        str+=s.pop()
    return str


print(demo(56556,16))
print(demo(152,8))