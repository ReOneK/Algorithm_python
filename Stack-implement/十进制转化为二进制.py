"""
十进制转换为二进制

"""

from pythonds.basic.stack import Stack


def ten_to_two(num):
     s=Stack()
     while num>0:
          a=num%2
          s.push(a)
          num=num//2

     stringg=""
     while not s.isEmpty():
          stringg=stringg+str(s.pop())


     return stringg


print(ten_to_two(1235))
