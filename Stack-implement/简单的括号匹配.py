from pythonds.basic.stack import Stack

"""
只包含（）,不包含别的
"""

def stack_match(symbalstring):
     s=Stack()
     balance=True
     index=0
     while  index<len(symbalstring) and balance:
          if symbalstring[index]=="(":
               s.push(symbalstring[index])
          else:
               if s.isEmpty():
                    balance=False
               else:
                    s.pop()

          index+=1


     if balance and s.isEmpty():
          return True

     else:
          return False



print(stack_match('((()))'))
