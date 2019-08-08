from trees import *
from black_red_tree import left_rotate, right_rotate

class AVLNode(Node):
    def __init__(self, key, height=1, left=None, right=None, parent=None):
        super().__init__(key, left, right, parent)
        self.height = height

    def other_name(self, level=0, lrFlag=0):
        if lrFlag == 0:
            specSym = ''
        elif lrFlag == -1:
            specSym = '|l|'
        else:
            specSym = '|r|'
        print('--' * level + specSym + str(self.key) + str(bfactor(self)))
        if self.left:
            self.left.other_name(level + 1, lrFlag=-1)
        if self.right:
            self.right.other_name(level + 1, lrFlag=1)

def height(node: AVLNode):
    return 0 if node is None else node.height

def bfactor(node: AVLNode):
    return height(node.right)-height(node.left)

def fixheight(node: AVLNode):
    hl = height(node.left)
    hr = height(node.right)
    node.height = (hl if hl > hr else hr) + 1

def avlleft_rotate(rootNode: AVLNode, x: AVLNode):
    rootNode = left_rotate(rootNode, x)
    fixheight(x)
    fixheight(x.parent)
    return rootNode


def avlright_rotate(rootNode: AVLNode, x: AVLNode):
    rootNode = right_rotate(rootNode, x)
    fixheight(x)
    fixheight(x.parent)
    return rootNode

def avlbalance(rootNode: AVLNode, node: AVLNode):
    x = node
    while x is not None:
        fixheight(x)
        bfact = bfactor(x)
        if bfact == 2:
            if x.right is not None and bfactor(x.right) < 0:
                rootNode = avlright_rotate(rootNode, x.right)
            rootNode = avlleft_rotate(rootNode, x)
            x = x.parent.parent
        elif bfact == -2:
            if x.left is not None and bfactor(x.left) > 0:
                rootNode = avlleft_rotate(rootNode, x.left)
            rootNode = avlright_rotate(rootNode, x)
            x = x.parent.parent
        else:
            x = x.parent
    return rootNode


def avlinsert(rootNode, node: AVLNode):
    return avlbalance(tree_insert(rootNode, node), node)

def avldelete(rootNode: AVLNode, node: AVLNode):
    y = z if z.left is None or z.right is None else tree_successor(z)
    x = y.left if y.left is not None else y.right
    if x is not None:
        x.parent = y.parent
    if y.parent is None:
        rootNode = x
    elif y == y.parent.left:
        y.parent.left, lrFlag = x, -1
    else:
        y.parent.right, lrFlag = x, 1
    nodeFather = y.parent
    if y != z:  # Если мы переместили в вершину z вершину y
        z.key = y.key
    return avlbalance(rootNode, nodeFather)

rootNode = z = AVLNode(8)
rootNode = avlinsert(rootNode, AVLNode(3))
rootNode = avlinsert(rootNode, AVLNode(4))
rootNode = avlinsert(rootNode, AVLNode(1))
rootNode = avlinsert(rootNode, AVLNode(3.5))
rootNode = avldelete(rootNode, z)
