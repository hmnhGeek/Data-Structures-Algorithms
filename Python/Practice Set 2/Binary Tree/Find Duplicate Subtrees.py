# Problem link - https://www.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1
# Solution - https://www.youtube.com/watch?v=m0dG99f5ct4


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _find(root: Node, result, mp):
        if root is None:
            return "N"
        s = f"{root.data}" + "," + Solution._find(root.left, result, mp) + "," + Solution._find(root.right, result, mp)
        if s in mp and mp[s] == 1:
            result.add(s)
        elif s not in mp:
            mp[s] = 1
        else:
            mp[s] += 1
        return s

    @staticmethod
    def get_duplicates(root: Node):
        # Time complexity is O(N^2) because we are visiting every node again and again for each subtree
        # Space complexity is O(N).
        result = set()
        mp = dict()
        Solution._find(root, result, mp)
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