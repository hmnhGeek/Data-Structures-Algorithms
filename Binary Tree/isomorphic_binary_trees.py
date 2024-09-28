# Problem link - https://www.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1
# Solution - https://www.youtube.com/watch?v=9Eo42meRcrY


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def are_isomorphic(root1: Node, root2: Node) -> bool:
    # if both the trees are empty, then they are isomorphic
    if root1 is None and root2 is None:
        return True
    # if one of the trees are empty, but the other is not, then they are not isomorphic
    if root1 is None or root2 is None:
        return False
    # if both the trees are not empty, then check if the data on the current node matches or not.
    # if the data does not match, return False as they are not isomorphic.
    if root1.data != root2.data:
        return False

    # finally, if the data on both the root nodes are same, use recursion on subtrees.
    # if the left subtree of 1st tree is same as left subtree of 2nd tree and right subtree of 1st tree is
    # same as right subtree of 2nd tree, then the subtrees are same-isomorphic.
    are_same_isomorphic = are_isomorphic(root1.left, root2.left) and are_isomorphic(root1.right, root2.right)
    # or, if the left subtree of 1st tree is same as right subtree of 2nd tree and vice versa, then they are
    # cross-isomorphic.
    are_cross_isomorphic = are_isomorphic(root1.left, root2.right) and are_isomorphic(root1.right, root2.left)
    # return true if the trees are either same-isomorphic or cross-isomorphic.
    return are_same_isomorphic or are_cross_isomorphic


# Example 1
one, two, three, four = Node(1), Node(2), Node(3), Node(4)
one1, two1, three1, four1 = Node(1), Node(2), Node(3), Node(4)
one.left = two
two.left = four
one.right = three
one1.left = three1
three1.left = four1
one1.right = two1
print(are_isomorphic(one, one1))

# Example 2
one, two, three, four = Node(1), Node(2), Node(3), Node(4)
one1, two1, three1, four1 = Node(1), Node(2), Node(3), Node(4)
one.left = two
two.left = four
one.right = three
one1.left = three1
one1.right = two1
two1.right = four1
print(are_isomorphic(one, one1))