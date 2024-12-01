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
        if counter[0] < n and Solution._is_digit(string[counter[0]]):
            _sum = 0
            while counter[0] < n and Solution._is_digit(string[counter[0]]):
                _sum += int(string[counter[0]])
                counter[0] += 1
            root.data = _sum

        if counter[0] < n and string[counter[0]] == "(":
            root.left = TreeNode(None)
            counter[0] += 1
            Solution._solve(root.left, string, counter, n)
        if counter[0] < n and string[counter[0]] == "(":
            root.right = TreeNode(None)
            counter[0] += 1
            Solution._solve(root.right, string, counter, n)
        if counter[0] < n and string[counter[0]] == ")":
            counter[0] += 1
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
        dummy_node = TreeNode(None)
        counter = [0]
        Solution._solve(dummy_node, string, counter, len(string))
        inorder = []
        Solution._inorder(dummy_node, inorder)
        return inorder


print(Solution.get_tree("1(2)(3)"))
print(Solution.get_tree("4(2(3)(1))(6(5))"))
print(Solution.get_tree("4(2(3(1)))(5)"))
print(Solution.get_tree("1(2(4)(5))(3(6)(7))"))
