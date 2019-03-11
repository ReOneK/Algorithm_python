"""
中缀表达式转换成后缀表达式
"""

from pythonds.basic.stack import Stack

def exchange_express(expression):
     s=Stack()
     nums=[]
     pre={}
     pre['/']=3
     pre['*']=3
     pre['+']=2
     pre['-']=2
     pre['(']=1
     tokenlist=expression.split()

     for token in tokenlist:
          if token=="(":
               s.push(token)

          elif token in "0123456789" or token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
               nums.append(token)

          elif token==")":
               a=s.pop()
               if not a=="(":
                    nums.append(a)
                    a=s.pop()

          else:
               while (not s.isEmpty()) and pre[s.peek()]>=pre[token]:
                    nums.append(s.pop())
               s.push(token)

     while not s.isEmpty():
          nums.append(s.pop())
     return ''.join(nums)


print(exchange_express("A * B + C * D"))
