# Problem link - https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/
# Solution - https://www.youtube.com/watch?v=hZnDglRWunk


class TreeNode:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class Solution:
    @staticmethod
    def _is_digit(x):
        try:
            int(x)
            return True
        except:
            return False

    @staticmethod
    def _solve(root: TreeNode, string: str, counter, n):
        # if the current character is a digit, extract the full number using a while loop.
        if counter[0] < n and Solution._is_digit(string[counter[0]]):
            _sum = 0
            while counter[0] < n and Solution._is_digit(string[counter[0]]):
                _sum = _sum * 10 + int(string[counter[0]])
                counter[0] += 1
            # once the number is extracted, assign it to root's data.
            root.data = _sum

        # if for this root, this is the first opening bracket, build the left subtree.
        if counter[0] < n and string[counter[0]] == "(":
            root.left = TreeNode(None)
            counter[0] += 1
            Solution._solve(root.left, string, counter, n)

        # if for this root, this is the second opening bracket, build the right subtree.
        if counter[0] < n and string[counter[0]] == "(":
            root.right = TreeNode(None)
            counter[0] += 1
            Solution._solve(root.right, string, counter, n)

        # if for this root, a closing bracket is found, do not return, simply move to the next character
        if counter[0] < n and string[counter[0]] == ")":
            counter[0] += 1

        # if string is exhausted, return.
        if counter[0] >= n:
            return

    @staticmethod
    def _inorder(root: TreeNode, inorder):
        if root:
            Solution._inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._inorder(root.right, inorder)

    @staticmethod
    def get_tree(string: str):
        """
            Time complexity is O(n) and space complexity is O(h).
        """

        # create a starting dummy node.
        dummy_node = TreeNode(None)

        # store a reference counter to track the string.
        counter = [0]

        # recursively call the solve function to build the tree.
        Solution._solve(dummy_node, string, counter, len(string))

        # finally return the preorder traversal of the tree.
        inorder = []
        Solution._inorder(dummy_node, inorder)
        return inorder


print(Solution.get_tree("1(2)(3)"))
print(Solution.get_tree("4(2(3)(1))(6(5))"))
print(Solution.get_tree("4(2(3(1)))(5)"))
print(Solution.get_tree("1(2(4)(5))(3(6)(7))"))
