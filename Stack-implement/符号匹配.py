"""
符号匹配

"""
from pythonds.basic.stack import Stack
def symbal_match1(symbal):
     s=Stack()
     index=0
     balance=True
     while index<len(symbal_match1) and balance:
          a=symbal_match1[index]
          if a in "([{":
               s.push(a)
          else:
               if s.isEmpty():
                    balance=False

               else:
                    a=s.pop()
                    if not match(a,symbal):
                         balance=False

          index+=1

     if balance and s.isEmpty():
          return True
     else:
          return False


def match(left,right):
     lefts="([{"
     rights=")]}"
     return lefts.index[left]==rights.index[right]
