class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Preorder:
    @staticmethod
    def _recursive(root: Node, preorder):
        if root:
            preorder.append(root.data)
            Preorder._recursive(root.left, preorder)
            Preorder._recursive(root.right, preorder)

    @staticmethod
    def recursive(root: Node):
        preorder = []
        Preorder._recursive(root, preorder)
        return preorder


# Example 1
n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.left = n2
n2.left = n4
n3.left = n5
n5.left = n7
n1.right = n3
n3.right = n6
n5.right = n8
print(Preorder.recursive(n1))