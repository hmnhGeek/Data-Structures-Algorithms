# Problem link - https://www.geeksforgeeks.org/problems/construct-tree-1/1
# Solution - https://www.youtube.com/watch?v=aZNaLrVebKQ


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def construct(inorder, preorder):
        # pass full inorder and preorder to the _build method.
        return Solution._build(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1)

    @staticmethod
    def _build(inorder, in_start, in_end, preorder, pre_start, pre_end):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # if either of the inorder or preorder is exhausted, return null.
        if in_start > in_end or pre_start > pre_end:
            return None

        # since the start of the preorder is the root node, assign a new node for it.
        root = Node(preorder[pre_start])

        # get the index of this root node in the inorder traversal.
        inorder_index_of_root = inorder.index(root.data)

        # get the number of nodes in the left subtree
        nums_left = inorder_index_of_root - in_start

        # assign the left subtree of the root. Here, the inorder will start from the in_start, and go till the index
        # just before the index of the root node in the inorder traversal. Also, for preorder, the start pointer will
        # point to the next index of the root, i.e., pre_start + 1 and go till the left subtree size obtained from the
        # inorder traversal, i.e., pre_start + nums_left.
        root.left = Solution._build(
            inorder, in_start, inorder_index_of_root - 1,
            preorder, pre_start + 1, pre_start + nums_left
        )

        # assign the right subtree of the root. Here, the inorder will start from the next index of the root from the
        # inorder, and go till the in_end index. Also, for preorder, the start pointer will start from left subarray end
        # and go till pre_end index.
        root.right = Solution._build(
            inorder, inorder_index_of_root + 1, in_end,
            preorder, pre_start + nums_left + 1, pre_end
        )

        # finally return the root.
        return root


# Example 1
t1 = Solution.construct([1, 6, 8, 7], [1, 6, 7, 8])
print(t1.left, t1.right.data)
print(t1.right.left, t1.right.right.data)
print(t1.right.right.left.data, t1.right.right.right)