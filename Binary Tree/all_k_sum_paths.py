# Problem link - https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
# Solution - https://www.youtube.com/watch?v=7oL8kDCk1OI
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def get_contagious_paths(root, path, target):
    '''
    The basic idea to solve the problem is to do a preorder traversal of the given tree. We also need a container (
    vector) to keep track of the path that led to that node. At each node we check if there are any path that sums to
    k, if any we print the path and proceed recursively to print each path.
    '''
    if root is None:
        return

    path.append(root.data)
    get_contagious_paths(root.left, path, target)
    get_contagious_paths(root.right, path, target)

    _sum = 0
    for i in range(-1, -len(path) - 1, -1):
        _sum += path[i]
        if _sum == target:
            print(path[i::], end=" ")
    path.pop(-1)


def get_tree_path_sum_equals_k(root: Node, k: int):
    paths = []
    return get_contagious_paths(root, paths, k)


one, three, minus_one, two, one_ro_three, one_ro_lo_three, four, one_lo_four, two_ro_four, five, six = Node(1), Node(3), Node(-1), Node(2), Node(1), Node(1), Node(4), Node(1), Node(2), Node(5), Node(6)

one.left = three
three.left = two
one_ro_three.left = one_ro_lo_three
minus_one.left = four
four.left = one_lo_four

one.right = minus_one
three.right = one_ro_three
four.right = two_ro_four
minus_one.right = five
five.right = six

get_tree_path_sum_equals_k(one, 5)
