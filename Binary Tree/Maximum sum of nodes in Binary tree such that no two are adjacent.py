class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def recursive():
    def solve(root: Node, pick: bool):
        if root is None:
            return 0
        left = solve(root.left, not pick)
        right = solve(root.right, not pick)
        result = left + right
        if pick:
            result += root.data
        return result

    def get_max_sum(root: Node):
        return max(solve(root, True), solve(root, False))

    # Example 1
    one, two, three, one1, four, five = Node(1), Node(2), Node(3), Node(1), Node(4), Node(5)
    one.left = two
    two.left = one1
    three.left = four

    one.right = three
    three.right = five
    print(get_max_sum(one))


recursive()