# Problem link - https://www.geeksforgeeks.org/problems/duplicate-subtrees/1
# Solution - https://www.youtube.com/watch?v=m0dG99f5ct4


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def find_duplicate_subtrees(root: Node):
        # Time complexity is O(N^2) because we are visiting every node again and again for each subtree
        # Space complexity is O(N).
        mp = {}
        result = []
        Solution.solve(root, mp, result)
        print(result)

    @staticmethod
    def solve(root, mp, result):
        if root is None:
            return "N"
        s = str(root.data) + "," + Solution.solve(root.left, mp, result) + "," + Solution.solve(root.right, mp, result)
        if s in mp:
            if mp[s] == 1:
                result.append(s)
            mp[s] += 1
        else:
            mp[s] = 1
        return s


# Example 1
one, two, three, four, two1, four2, four3 = Node(1), Node(2), Node(3), Node(4), Node(2), Node(4), Node(4)
one.left = two
two.left = four
three.left = two1
two1.left = four3
one.right = three
three.right = four2
Solution.find_duplicate_subtrees(one)
print()

# Example 2
five, four, six, three, four2, three2, six2 = Node(5), Node(4), Node(6), Node(3), Node(4), Node(3), Node(6)
five.left = four
four.left = three
four2.left = three2
five.right = six
four.right = four2
four2.right = six2
Solution.find_duplicate_subtrees(five)
