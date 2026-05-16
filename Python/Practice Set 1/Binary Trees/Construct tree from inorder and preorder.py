# Problem link - https://www.geeksforgeeks.org/problems/construct-tree-1/1
# Solution - https://www.youtube.com/watch?v=G5c1wM3Kpuw


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def construct(preorder, inorder) -> Node:
        """
            Time complexity is O(n^2) {for iterating in both inorder and preorder arrays) and space complexity is O(n).
        """

        n = len(inorder)
        if n != len(preorder):
            return None

        # we need to pass index by reference so that it does not lose its incremental value
        # in the preorder array, that is, it does not go back to some prior value according to
        # the recursion stack. It should always move forward.
        index = [0]

        # search space in inorder array is [0, n - 1] with index pointing to preorder array.
        return Solution._solve(preorder, inorder, 0, n - 1, index)

    @staticmethod
    def _solve(preorder, inorder, start, end, index) -> Node:
        # if this happens, you're on a leaf node, return its left or right child as null.
        if start > end:
            return None

        # get the data from preorder array.
        data = preorder[index[0]]

        # find this data point in inorder array.
        for i in range(start, end + 1):
            if inorder[i] == data:
                break

        # now create the root node.
        root = Node(data)

        # increment the index in preorder array.
        index[0] += 1

        # get the left and right children of the root node and return it.
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
Solution.test([1, 4, 5, 2, 3], [2, 5, 4, 1, 3])
