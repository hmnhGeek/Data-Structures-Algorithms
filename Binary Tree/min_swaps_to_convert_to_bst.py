# Problem link - https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _get_inorder(root: Node, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def _get_min_swaps(inorder: list):
        """
            Time complexity is O(n*log(n)) and space complexity is O(n).
        """

        # get the temp list in O(n) space and O(n) time.
        temp = [(inorder[i], i) for i in range(len(inorder))]
        # sort the list in O(n*log(n)) time.
        temp.sort(key=lambda x: x[0])

        # loop on the temp list in n iterations
        i = 0
        swaps = 0
        while i < len(temp):
            elem, index = temp[i]
            # if a swap is needed, perform the swap and increment the swap count and stay on the same i.
            if index != i:
                temp[index], temp[i] = temp[i], temp[index]
                swaps += 1
            else:
                # else if element is in correct index, increment i.
                i += 1

        # return the count of swaps performed to get back the original temp before sorting.
        return swaps

    @staticmethod
    def get_min_swaps(root: Node):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        inorder = []
        # get the inorder of the tree in O(n) time and O(h) space.
        Solution._get_inorder(root, inorder)
        # in O(n * log(n)) time and O(n) space get the min swaps needed.
        return Solution._get_min_swaps(inorder)


# Example 1
n5, n6, n7, n8, n9, n10, n11 = Node(5), Node(6), Node(7), Node(8), Node(9), Node(10), Node(11)
n5.left = n6
n5.right = n7
n6.left = n8
n6.right = n9
n7.left = n10
n7.right = n11
print(Solution.get_min_swaps(n5))


# Example 2
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
print(Solution.get_min_swaps(n1))
