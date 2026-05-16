class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def construct(preorder, inorder) -> Node:
        n = len(inorder)
        if n != len(preorder):
            return None
        index = [0]
        return Solution._solve(preorder, inorder, 0, n - 1, index)

    @staticmethod
    def _solve(preorder, inorder, start, end, index) -> Node:
        if start > end:
            return None
        data = preorder[index[0]]
        for i in range(start, end + 1):
            if inorder[i] == data:
                break
        root = Node(data)
        index[0] += 1
        root.left = Solution._solve(preorder, inorder, start, i - 1, index)
        root.right = Solution._solve(preorder, inorder, i + 1, end, index)
        return root

    @staticmethod
    def get_postorder(root: Node, postorder):
        if root:
            Solution.get_postorder(root.left, postorder)
            Solution.get_postorder(root.right, postorder)
            postorder.append(root.data)

    @staticmethod
    def test(preorder, inorder):
        root = Solution.construct(preorder, inorder)
        postorder = []
        Solution.get_postorder(root, postorder)
        print(postorder)


Solution.test([0, 1, 3, 4, 2, 5], [3, 1, 4, 0, 5, 2])