#Binary Tree Node
class BinaryTreeNode(object):
    def __init__(self):
        self.data ='#'
        self.leftChild = None
        self.rightChild = None

class BinaryTree(object):
#create a binary tree
    def createBinaryTree(self, Root):
        data = input('==>')
        if data =='#':
            Root = None
        else:
            Root.data = data
            Root.leftChild = BinaryTreeNode() #Creates the left child
            self.createBinaryTree(Root.leftChild) #creates the left child's Binary tree
            Root.rightChild = BinaryTreeNode() #Creates the right child
            self.createBinaryTree(Root.rightChild) #Creates the right child's Binary Tree

#There are three ways to traverse a binary tree

    def preOrder(self, Root):
        if Root is not None:
            self.visitBinaryTreeNode(Root)
            self.preOrder(Root.leftChild)
            self.preOrder(Root.rightChild)

    def inOrder(self,Root):
        if Root is not None:
            self.inOrder(Root.leftChild)
            self.visitBinaryTreeNode(Root)
            self.inOrder(Root.rightChild)

    def postOrder(self,Root):
        if Root is not None:
            self.postOrder(Root.leftChild)
            self.postOrder(Root.rightChild)
            self.visitBinaryTreeNode(Root)

    def visitBinaryTreeNode(self, BinaryTreeNode):
        #pound sign # means empty node
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data, end= "->")

bTN = BinaryTreeNode()
bT = BinaryTree()
bT.createBinaryTree(bTN)
print('pre_order: ')
bT.preOrder(bTN)
print('\nIn_order: ')
bT.inOrder(bTN)
print('\nPost_order: ')
bT.postOrder(bTN)

