# Instructions
#
# t = Tree()
# t.add(2)
# t.add(5)
# t.add(1)
# t.add(4)
# t.add(3)
# t.add(6)
# t.printTree()
# t.deleteTree()
#
# t2 = Tree()
# t2.addByList([1,2,5,4,8,10])
# t2.printTree()

class TreeNode(object):
    # Definition for a binary tree node.
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addByList(self, valList):
        self.root = TreeNode(valList[0])
        for x in xrange(1,len(valList)):
            self._add(valList[x], self.root)

    def add(self, val):
        if(self.root == None):
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.value):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = TreeNode(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = TreeNode(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.value):
            return node
        elif(val < node.value and node.left != None):
            self._find(val, node.left)
        elif(val > node.value and node.right != None):
            self._find(val, node.right)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print str(node.value) + ' '
            self._printTree(node.right)
