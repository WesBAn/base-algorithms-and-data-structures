from trees.black_red_tree import *
"""
Not realized at all!
"""

class OrderRBNode(RBNode):
    def __init__(self, key, color, size=1, left=None, right=None, parent=None):
        super().__init__(key, color, left, right, parent)
        self.size = size

def fixsize(rootNode: OrderRBNode, node: OrderRBNode):
    node.size = (node.left.size if node.left is not None else 0) +\
                (node.right.size if node.right is not None else 0) + 1
    return rootNode

def orb_insert(rootNode: OrderRBNode, z: OrderRBNode):
    rootNode = rbtree_insert(rootNode, z)
    while z is not None:
        rootNode = fixsize(rootNode, z)
        z = z.parent






def os_select(x: OrderRBNode, i):
    if x is None:
        return None
    r = (x.left.size if x.left is not None else 0) + 1
    if i == r:
        return x
    elif i < r:
        return os_select(x.left, i)
    else:
        return os_select(x.right, i - r)