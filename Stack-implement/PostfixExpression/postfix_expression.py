from stack import Stack
import re


Token={'(': 5, '*': 4, '/': 3, '+': 2, '-': 1}
Pattern=re.compile('\d')


token_stack = Stack()
number_stack = Stack()


def Postfix(expression):
    result = []
    pre_char=None
    if not isinstance(expression,str):
        raise TypeError("your input is wrong")
    for char in expression:
        if char in Token:
            pre_token=token_stack.peek()
            while pre_token and Token[char] <= Token[pre_token]:
                if pre_token == '(':
                    break
                result.append(token_stack.pop())
                pre_token=token_stack.peek()
            token_stack.push(char)

        elif char==')':
            pre_token = token_stack.peek()
            while pre_token!='(':
                pre_token=token_stack.pop()
                result.append(pre_token)
                pre_token=token_stack.peek()
            token_stack.pop()
        elif Pattern.match(char):
            if pre_char and Pattern.match(pre_char):
                result[len(result)-1]+=char
            else:
                result.append(char)
        else:
            raise TypeError("Unsupport Type")
        pre_char=char
    while not token_stack.empty():
        result.append(token_stack.pop())
    return result


def count(result):
    if not isinstance(result,list):
        raise TypeError("Unsupport Type")
    for element in result:
        if element in Token:
            num1 = number_stack.pop()
            num2 = number_stack.pop()
            eval_result = num2+element+num1
            number_stack.push(str(eval(eval_result)))
        else:
            try:
                number_stack.push(element)
            except TypeError as e:
                print("Unsupport Type")
    return number_stack


if __name__ == '__main__':
    print(Postfix('70+2*10*(5-1*2-3/(1+40))'))
    print(count(Postfix('70+2*10*(5-1*2-3/(1+40))')))

