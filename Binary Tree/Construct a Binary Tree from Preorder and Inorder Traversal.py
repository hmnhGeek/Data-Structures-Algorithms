class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def construct(inorder, preorder):
        return Solution._build(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1)

    @staticmethod
    def _build(inorder, in_start, in_end, preorder, pre_start, pre_end):
        if in_start > in_end or pre_start > pre_end:
            return None
        root = Node(preorder[pre_start])
        inorder_index_of_root = inorder.index(root.data)
        nums_left = inorder_index_of_root - in_start
        root.left = Solution._build(
            inorder, in_start, inorder_index_of_root - 1,
            preorder, pre_start + 1, pre_start + nums_left
        )
        root.right = Solution._build(
            inorder, inorder_index_of_root + 1, in_end,
            preorder,pre_start + nums_left + 1, pre_end
        )
        return root


# Example 1
t1 = Solution.construct([1, 6, 8, 7], [1, 6, 7, 8])
print(t1.left, t1.right.data)
print(t1.right.left, t1.right.right.data)
print(t1.right.right.left.data, t1.right.right.right)