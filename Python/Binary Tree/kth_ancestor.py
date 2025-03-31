# Problem link - https://www.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kth_ancestor(root, node, k):
    # The whole operation would take O(N) time and O(H) space.

    if root is None:
        return None

    # if root is the same as node which we are trying to find, start by returning 1, representing
    # the 1st parent at the returned position
    if root == node:
        return 1

    left = kth_ancestor(root.left, node, k)
    # if the left recursion finds a node, and you're getting an integer equal to k,
    # then you must be at the kth ancestor, return this node.
    if left == k:
        return root

    # same logic for right recursion as above.
    right = kth_ancestor(root.right, node, k)
    if right == k:
        return root

    # now, let's assume that both left and right did not return value `k` above, then
    # at last, we would come here.

    # if left and right both are None, you return None
    if left is None and right is None:
        return None
    if left is None:
        # if left is None, right must be non-None. Now here we have two possibilities
        # 1. right is a number: if it is, then, since right != k, we have not found the kth
        #    ancestor, and therefore, we return right + 1.
        # 2. right is a Node: if it is, then simply return it as a node only. It would happen
        #    only if we have found the kth ancestor in right recursion. So we must propagate
        #    this node upwards until the final recursion ends.
        return 1 + right if type(right) == type(1) else right
    if right is None:
        # same logic as above in the left recursion.
        return 1 + left if type(left) == type(1) else left


def example1():
    one, two, three, four, five = Node(1), Node(2), Node(3), Node(4), Node(5)
    one.left = two
    two.left = four
    one.right = three
    two.right = five
    node = kth_ancestor(one, five, 2)
    # if the kth ancestor, i.e., node is an integer, then it means we were unable to find
    # a node which is a kth ancestor. Therefore, print -1.
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
    node = kth_ancestor(two, nine, 3)
    # if the kth ancestor, i.e., node is an integer, then it means we were unable to find
    # a node which is a kth ancestor. Therefore, print -1.
    if type(node) == Node:
        print(node.data)
    else:
        print(-1)


example1()
example2()