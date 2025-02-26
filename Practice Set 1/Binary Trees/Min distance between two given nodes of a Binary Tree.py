class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _lca(root: Node, node1, node2):
        if root is None:
            return
        if root.data == node1 or root.data == node2:
            return root
        left = Solution._lca(root.left, node1, node2)
        right = Solution._lca(root.right, node1, node2)

        if left is None and right is None:
            return
        if left is None:
            return right
        if right is None:
            return left
        return root
    
    @staticmethod
    def _get_distance(root: Node, node, level, distance):
        if root is None:
            return
        if root.data == node:
            distance[0] = min(distance[0], level)
            return
        Solution._get_distance(root.left, node, level + 1, distance)
        Solution._get_distance(root.right, node, level + 1, distance)
        
    @staticmethod
    def get_min_distance(root: Node, node1, node2):
        """
            Overall time complexity is O(n) and overall space complexity is O(n).
        """

        # Get LCA in O(n) time and O(n) space.
        lca = Solution._lca(root, node1, node2)

        # get the distance of node1 and node2 from LCA in O(n) time and O(n) space.
        d1 = [1e6]
        d2 = [1e6]
        Solution._get_distance(lca, node1, 0, d1)
        Solution._get_distance(lca, node2, 0, d2)

        # return the minimum distance.
        return d1[0] + d2[0]
    

def example1():
    el, twtwo, ththr, ff, fifv, sixsix, svnsvn = Node(11), Node(22), Node(33), Node(44), Node(55), Node(66), Node(77)
    el.left = twtwo
    twtwo.left = ff
    ththr.left = sixsix
    el.right = ththr
    twtwo.right = fifv
    ththr.right = svnsvn
    print(Solution.get_min_distance(el, 77, 22))


def example2():
    one, two, three = Node(1), Node(2), Node(3)
    one.left = two
    one.right = three
    print(Solution.get_min_distance(one, 2, 3))


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

    print(Solution.get_min_distance(root, 7, 9))


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

    print(Solution.get_min_distance(root, 4, 1))


def example5():
    # Creating nodes
    root = Node(5)
    three = Node(3)
    six = Node(6)
    two = Node(2)
    four = Node(4)
    seven = Node(7)
    one = Node(1)
    eight = Node(8)

    # Constructing the tree
    root.left = three
    root.right = six

    three.left = two
    three.right = four

    six.right = seven

    two.left = one
    seven.right = eight

    print(Solution.get_min_distance(root, 1, 8))


print("\nExample 1")
example1()
print("\n\nExample 2")
example2()
print("\n\nExample 3")
example3()
print("\n\nExample 4")
example4()
print("\n\nExample 5")
example5()
        