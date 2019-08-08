class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.left: Node = left
        self.right: Node = right
        self.parent: Node = parent
        self.key = key


def inorder_tree_walk(x: Node):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)

def tree_search(x: Node, k):
    if x is None or k == x.key:
        return x
    return tree_search(x.left, k) if k < x.key else tree_search(x.right, k)

def iterative_tree_search(x: Node, k):
    while x is not None and k != x.key:
        x = x.left if k < x.key else x.right
    return x

def tree_minimum(x: Node):
    while x.left is not None:
        x = x.left
    return x

def tree_maximum(x: Node):
    while x.right is not None:
        x = x.right
    return x

def tree_successor(x: Node):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x, y = y, y.parent
    return y

def tree_insert(rootNode: Node, z: Node):
    x = rootNode
    y = None
    while x is not None:
        y = x
        x = x.left if z.key <= x.key else x.right
    z.parent = y
    if y is None:
        return z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return rootNode

def tree_delete(rootNode: Node, z: Node) -> Node:
    y = z if z.left is None or z.right is None else tree_successor(z)
    x = y.left if y.left is not None else y.right
    if x is not None:
        x.parent = y.parent
    if y.parent is None:
        rootNode = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    if y != z:
        z.key = y.key
    return rootNode

if __name__ == '__main__':
    root = Node(10)
    z = Node(6)
    tree_insert(root, z)
    tree_insert(root, Node(5))
    tree_insert(root, Node(5.5))
    tree_insert(root, Node(16))
    tree_insert(root, Node(11))
    tree_insert(root, Node(19))
    inorder_tree_walk(root)
    print('///')
    root = tree_delete(root, z)
