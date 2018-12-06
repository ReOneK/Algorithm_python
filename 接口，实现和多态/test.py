"""
测试两个包的实现
"""

from arraybag import Arraybag
from linkedbag import Linkedbag

def test(bagtype):
    lst=[2020,520,1314]
    print("the list of item add is:", lst)
    b1 = bagtype(lst)
    print("length 3 :", len(b1))

    print("Is or Not:", 2020 in b1)
    print("Is or Not:", 15 in b1)
    print("Iter:")
    for i in b1:
        print(i)

    b1.clear()
    print(b1)
    b1.add(25)
    print(b1)
    b1.remove(25)
    print(b1)


test(Arraybag)

