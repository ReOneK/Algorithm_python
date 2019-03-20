#前序外部实现
def preorder(parserTree):
    if parserTree:
        print(parserTree.getRootVal())
        preorder(parserTree.getLeftChild())
        preorder(parserTree.getRightChild())


#前序内部实现
def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()


#后序实现
def underorder(parsetree):
    if parsetree:
        preorder(parsetree.getLeftChild())
        preorder(parsetree.getRightChild())
        print(parsetree.getRootVal())


#中序实现
def inorder(parsetree):
  if parsetree != None:
      inorder(parsetree.getLeftChild())
      print(parsetree.getRootVal())
      inorder(parsetree.getRightChild())



