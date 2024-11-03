class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class PostOrder:
    @staticmethod
    def _recursive(root: Node, postorder):
        if root:
            PostOrder._recursive(root.left, postorder)
            PostOrder._recursive(root.right, postorder)
            postorder.append(root.data)

    @staticmethod
    def recursive(root: Node):
        postorder = []
        PostOrder._recursive(root, postorder)
        return postorder

