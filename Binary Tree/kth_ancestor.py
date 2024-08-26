class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kth_ancestor(root, node, k, ht):
    if root is None:
        return None

    if root == node:
        return 1

    left = kth_ancestor(root.left, node, k, ht + 1)
    if left == k:
        return root

    right = kth_ancestor(root.right, node, k, ht + 1)
    if right == k:
        return root

    if left is None and right is None:
        return None
    if left is None:
        return 1 + right if type(right) == type(1) else right
    if right is None:
        return 1 + left if type(left) == type(1) else left


def example1():
    one, two, three, four, five = Node(1), Node(2), Node(3), Node(4), Node(5)
    one.left = two
    two.left = four
    one.right = three
    two.right = five
    node = kth_ancestor(one, five, 2, 0)
    if type(node) == Node:
        print(node.data)
    else:
        print(-1)


def example2():
    eight, two, six, seven, zero, five, nine = Node(8), Node(2), Node(6), Node(7), Node(0), Node(5), Node(9)
    two.left = eight
    six.left = seven
    eight.right = five
    two.right = six
    six.right = zero
    zero.right = nine
    node = kth_ancestor(two, nine, 3, 0)
    if type(node) == Node:
        print(node.data)
    else:
        print(-1)


example2()