"""
十进制转换为八进制/十六进制
"""

from pythonds.basic.stack import Stack


def change_digits(num,mode):
     s=Stack()
     all_nums="0123456789ABCDEF"
     while num>0:
          a=num%mode
          s.push(a)
          num=num//mode

     stringg=""
     while not s.isEmpty():
          stringg=stringg+all_nums[s.pop()]

     return stringg


print(change_digits(152666,16))
