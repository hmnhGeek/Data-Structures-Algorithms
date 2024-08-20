class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_distance(root: Node, node: Node, distance: int):
    if root is None:
        return

    if root.data == node.data:
        return distance

    left_dist = find_distance(root.left, node, distance + 1)
    right_dist = find_distance(root.right, node, distance + 1)

    if left_dist is not None:
        return left_dist
    if right_dist is not None:
        return right_dist
    return None


def get_lcs(root: Node, node1: Node, node2: Node):
    if root is None:
        return

    if root.data == node1.data:
        return root

    if root.data == node2.data:
        return root

    left = get_lcs(root.left, node1, node2)
    right = get_lcs(root.right, node1, node2)

    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    if right is not None:
        return right
    return None


def shortest_path(root, node1, node2):
    lcs = get_lcs(root, node1, node2)
    d1 = find_distance(lcs, node1, 0)
    d2 = find_distance(lcs, node2, 0)
    return d1 + d2


def example1():
    el, twtwo, ththr, ff, fifv, sixsix, svnsvn = Node(11), Node(22), Node(33), Node(44), Node(55), Node(66), Node(77)
    el.left = twtwo
    twtwo.left = ff
    ththr.left = sixsix
    el.right = ththr
    twtwo.right = fifv
    ththr.right = svnsvn
    print(shortest_path(el, svnsvn, twtwo))


def example2():
    one, two, three = Node(1), Node(2), Node(3)
    one.left = two
    one.right = three
    print(shortest_path(one, two, three))


def example3():
    # Creating nodes
    root = Node(2)
    seven = Node(7)
    five = Node(5)
    two = Node(2)
    six = Node(6)
    five_leaf = Node(5)
    eleven = Node(11)
    nine = Node(9)
    four = Node(4)

    # Constructing the tree
    root.left = seven
    root.right = five

    seven.left = two
    seven.right = six

    six.left = five_leaf
    six.right = eleven

    five.right = nine
    nine.left = four

    print(shortest_path(root, seven, nine))


example3()