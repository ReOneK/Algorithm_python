from pythonds.basic.deque import Deque

def check(input):
    d=Deque()
    for i in input:
        d.addFront(i)

    result=True
    while d.size() > 1 and result:
        top=d.removeFront()
        end=d.removeRear()
        if top!=end:
            result=False

    return result



print(check("lsdkjfskf"))
print(check("radar"))

