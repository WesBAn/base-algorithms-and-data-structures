from trees.trees import *
RED = 1
BLACK = 0


class RBNode(Node):
    def __init__(self, key, color, left=None, right=None, parent=None):
        super().__init__(key, left, right, parent)
        self.color = color

    def other_name(self, level=0, lrFlag=0):
        if lrFlag == 0:
            specSym = ''
        elif lrFlag == -1:
            specSym = '|l|'
        else:
            specSym = '|r|'
        print('--' * level + specSym + str(self.key) + ('к' if self.color == RED else 'ч'))
        if self.left:
            self.left.other_name(level + 1, lrFlag=-1)
        if self.right:
            self.right.other_name(level + 1, lrFlag=1)


def left_rotate(rootNode: Node, x: Node):
    if x.right is None:
        raise KeyError
    y = x.right
    y.parent = x.parent
    x.right, x.parent = y.left, y
    if y.left is not None:
        y.left.parent = x
    y.left = x
    if y.parent is None:
        rootNode = y
    elif y.parent.left == x:
        y.parent.left = y
    else:
        y.parent.right = y
    return rootNode


def right_rotate(rootNode: Node, x: Node):
    if x.left is None:
        raise KeyError
    y = x.left
    y.parent = x.parent
    x.left, x.parent = y.right, y
    if y.right is not None:
        y.right.parent = x
    y.right = x
    if y.parent is None:
        rootNode = y
    elif y.parent.left == x:
        y.parent.left = y
    else:
        y.parent.right = y
    return rootNode

def grandparent(x: Node):
    return x.parent.parent if x.parent is not None else None

def uncle(x: Node):
    grand = grandparent(x)
    if grand is None:
        return None
    elif grand.left == x.parent:
        return grand.right
    else:
        return grand.left

def rbtree_insert(rootNode: RBNode, x: RBNode):
    rootNode: RBNode = tree_insert(rootNode, x)
    x.color = RED
    while x != rootNode and x.parent.color == RED:
        if x.parent == grandparent(x).left:
            if grandparent(x).right is not None and grandparent(x).right.color == RED:
                y = grandparent(x).right # Uncle
                x.parent.color, y.color = BLACK, BLACK
                grandparent(x).color = RED
                x = grandparent(x)
            else:
                if x == x.parent.right:
                    x = x.parent
                    rootNode = left_rotate(rootNode, x)
                x.parent.color = BLACK
                grandparent(x).color = RED
                rootNode = right_rotate(rootNode, grandparent(x))
        else:
            if grandparent(x).left is not None and grandparent(x).left.color == RED:
                y = grandparent(x).left # UNCLE
                x.parent.color, y.color = BLACK, BLACK
                grandparent(x).color = RED
                x = grandparent(x)
            else:
                if x == x.parent.left:
                    x = x.parent
                    rootNode = right_rotate(rootNode, x)
                x.parent.color = BLACK
                grandparent(x).color = RED
                rootNode = left_rotate(rootNode, grandparent(x))
    while rootNode.parent is not None:
        rootNode = rootNode.parent
    rootNode.color = BLACK
    return rootNode

def rbdelete_fixup(rootNode: RBNode, nodeUpper: RBNode, lrFlag: int):
    if rootNode is None:
        return rootNode
    if nodeUpper is None:
        rootNode.color = BLACK
        return rootNode
    sonDeleted = getattr(nodeUpper, 'left' if lrFlag == -1 else 'right')
    # Сын удаленного узла (СУ) Красный => перекрасим в черный
    if sonDeleted is not None and sonDeleted.color == RED:
        sonDeleted.color = BLACK
        return rootNode
    # Сын удаленного узла (СУ) Черный
    else:
        bro = getattr(nodeUpper, 'left' if lrFlag == 1 else 'right')
        # Дети брата черные и брат черный
        if bro.color == BLACK and \
                    (bro.left is None or bro.left.color == BLACK) and \
                    (bro.right is None or bro.right.color == BLACK):
                bro.color = RED
                nodeUpper.color = BLACK
        elif lrFlag == -1:
            # Если Брат красный
            if bro.color == RED:
                bro.color = BLACK
                nodeUpper.color = RED
                rootNode = left_rotate(rootNode, nodeUpper)
            else:
                # Если брат черный правый ребенок =  черный левый = красный
                if bro.color == BLACK and \
                    (bro.left is not None and bro.left.color == RED) and \
                    (bro.right is None or bro.right.color == BLACK):
                    bro.color = RED
                    bro.left = BLACK
                    rootNode = right_rotate(rootNode, bro)
                nodeUpper.right.right.color = BLACK
                nodeUpper.right.color = nodeUpper.color
                nodeUpper.color = BLACK
                rootNode = left_rotate(rootNode, nodeUpper)
        else:
            # Если Брат красный
            if bro.color == RED:
                bro.color = BLACK
                nodeUpper.color = RED
                rootNode = right_rotate(rootNode, nodeUpper) # edited
            else:
                # Если брат черный левый ребенок =  черный черный = красный
                if bro.color == BLACK and \
                        (bro.right is not None and bro.right.color == RED) and \
                        (bro.left is None or bro.left.color == BLACK):
                    bro.color = RED
                    bro.right = BLACK
                    rootNode = left_rotate(rootNode, bro)
                nodeUpper.left.left.color = BLACK
                nodeUpper.left.color = nodeUpper.color
                nodeUpper.color = BLACK
                rootNode = right_rotate(rootNode, nodeUpper)
        return rootNode

def rbtree_delete(rootNode: RBNode, z: RBNode) -> Node:
    lrFlag = 0
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
    if y != z: # Если мы переместили в вершину z вершину y
        z.key = y.key
    if y.color == BLACK:
        rootNode = rbdelete_fixup(rootNode, nodeFather, lrFlag)
    return rootNode




if __name__ == '__main__':
    root = Node(6)
    tree_insert(root, Node(2))
    tree_insert(root, Node(9))
    tree_insert(root, Node(8))
    tree_insert(root, Node(10))
    root = left_rotate(root, root)
    root = right_rotate(root, root)
    ...
    ...

    rbroot = RBNode(8, BLACK)
    rbroot = rbtree_insert(rbroot, RBNode(4, RED))
    rbroot = rbtree_insert(rbroot, RBNode(1, RED))
    rbroot = rbtree_insert(rbroot, RBNode(2, RED))
    rbroot = rbtree_insert(rbroot, RBNode(3, RED))
    rbroot = rbtree_insert(rbroot, RBNode(12, RED))
    rbroot = rbtree_insert(rbroot, RBNode(7, RED))
    rbroot = rbtree_insert(rbroot, RBNode(11, RED))
    rbroot = rbtree_insert(rbroot, RBNode(15, RED))
    rbroot.other_name()
    print('////////')
    rbroot = rbtree_delete(rbroot, rbroot)
    rbroot.other_name()

    #rbroot = rbtree_delete(rbroot, z)
    #rbroot.other_name()
