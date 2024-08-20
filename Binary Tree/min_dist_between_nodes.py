# Problem link - https://www.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_distance(root: Node, node: Node, distance: int):
    """
    This function returns the distance between the root node and the `node`. This function will take O(N) time because
    it will check for the match in all the nodes and O(log(N)) space because in the worst case, the stack space will
    only occupy the branch from root to a leaf node.

    :param root: The starting node through which we have to find the node by traversing.
    :param node: Destination node
    :param distance: recursive variable for tracking distance
    :return: the distance between root and node.
    """

    # if the node was not found in a path, return None
    if root is None:
        return

    # if the node was found, return whatever distance that we have till now.
    if root.data == node.data:
        return distance

    # recursively check for node in the left subtree by incrementing one step.
    left_dist = find_distance(root.left, node, distance + 1)
    # recursively check for node in the right subtree by incrementing one step.
    right_dist = find_distance(root.right, node, distance + 1)

    # if the node was found in left subtree, return the distance.
    if left_dist is not None:
        return left_dist

    # if the node was found in right subtree, return the distance.
    if right_dist is not None:
        return right_dist

    # else return None, the node was not found in the subtree of root.
    return None


def get_lca(root: Node, node1: Node, node2: Node):
    """
    This function returns the lowest common ancestor of nodes 1 and 2 in O(N) time (as we are checking for all the
    nodes in the tree) and O(log(N)) space.
    :param root: root node of the main tree
    :param node1: first node
    :param node2: second node
    :return: the lowest common ancestor of nodes node1 and node2.
    """
    if root is None:
        return

    if root.data == node1.data:
        return root

    if root.data == node2.data:
        return root

    left = get_lca(root.left, node1, node2)
    right = get_lca(root.right, node1, node2)

    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    if right is not None:
        return right
    return None


def shortest_path(root, node1, node2):
    """
    This function first calculates the LCA of both the nodes. The shortest path between the two nodes will surely
    contain the LCA of both the nodes. Overall time complexity is O(N) and overall space complexity is O(log(N)).
    :param root: The root of the main tree
    :param node1: first node
    :param node2: second node
    :return: the minimum distance between node1 and node2 in the tree.
    """

    # Takes O(N) time and O(log(N)) space to find the LCA of both the nodes.
    LCA = get_lca(root, node1, node2)

    # Takes O(N) time and O(log(N)) space, to find the distance from LCA to node1.
    d1 = find_distance(LCA, node1, 0)

    # Takes O(N) time and O(log(N)) space, to find the distance from LCA to node2.
    d2 = find_distance(LCA, node2, 0)

    # return the summed distance as the shortest path.
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


def example4():
    # Creating nodes
    root = Node(3)
    five = Node(5)
    one = Node(1)
    six = Node(6)
    two = Node(2)
    seven = Node(7)
    four = Node(4)

    # Constructing the tree
    root.left = five
    root.right = one

    five.left = six
    five.right = two

    two.left = seven
    two.right = four

    print(shortest_path(root, four, one))


print("\nExample 1")
example1()
print("\n\nExample 2")
example2()
print("\n\nExample 3")
example3()
print("\n\nExample 4")
example4()