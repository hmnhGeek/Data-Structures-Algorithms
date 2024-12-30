# Problem link - https://www.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1
# Solution - https://www.youtube.com/watch?v=m0dG99f5ct4


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _update_result(root: Node, result: set, hash_map: set):
        # Time complexity is O(N^2) because we are visiting every node again and again for each subtree
        # Space complexity is O(N).
        if root is None:
            return "N,"
        string = f"{root.data}," + Solution._update_result(root.left, result, hash_map) + Solution._update_result(root.right, result, hash_map)
        if string in hash_map:
            result.add(string)
        hash_map.add(string)
        return string

    @staticmethod
    def get_duplicates(root: Node):
        result = set()
        hash_map = set()
        Solution._update_result(root, result, hash_map)
        return result


# Example 1
one, two, three, four, two1, four2, four3 = Node(1), Node(2), Node(3), Node(4), Node(2), Node(4), Node(4)
one.left = two
two.left = four
three.left = two1
two1.left = four3
one.right = three
three.right = four2
print(Solution.get_duplicates(one))
print()

# Example 2
five, four, six, three, four2, three2, six2 = Node(5), Node(4), Node(6), Node(3), Node(4), Node(3), Node(6)
five.left = four
four.left = three
four2.left = three2
five.right = six
four.right = four2
four2.right = six2
print(Solution.get_duplicates(five))
