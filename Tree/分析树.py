from pythonds.basic.stack import Stack
from pythonds.trees import BinaryTree
import operator


def buildParseTree(stringlist):
    splist=stringlist.split()
    s=Stack()
    etree=BinaryTree('')
    s.push(etree)
    currenttree=etree
    for i in splist:
        if i=='(':
            currenttree.insertLeft('')
            s.push(currenttree)
            currenttree=currenttree.getLeftChild()

        elif i not in ['+','-','*','/']:
            currenttree.setRootVal(i)
            parent=s.pop()
            currenttree=parent

        elif i in ['+','-','*','/']:
            currenttree.setRootVal(i)
            currenttree.insertRight('')
            s.push(currenttree)
            currenttree=currenttree.getRightChild()

        elif i==")":
            currenttree=s.pop()

        else:
            raise ValueError

def evaluate(parsetree):
    ops={'+':operator.add,
         '-':operator.sub,
         '*':operator.mul,
         '/':operator.truediv}

    lefttree=parsetree.getLeftChild()
    righttree=parsetree.getRightChild()

    if lefttree and righttree:
        operat=ops[parsetree.getRootVal()]
        return operat(evaluate(lefttree),evaluate(righttree))

