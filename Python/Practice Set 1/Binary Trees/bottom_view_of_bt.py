# Problem link - https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
# Solution - https://www.youtube.com/watch?v=0FtVY6I4pB8


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_bottom_view(root: TreeNode):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        result = []
        d = {}
        mini, maxi = 1e6, -1e6
        stack = Stack()
        stack.push((root, 0, 0))
        while not stack.is_empty():
            node, level, vertical = stack.pop()
            mini = min(mini, vertical)
            maxi = max(maxi, vertical)

            # if the vertical is found for the first time, update it in dictionary.
            if vertical not in d:
                d[vertical] = (node, level)

            # if the popped node is on the same level, don't do any update, because the right node is automatically
            # pushed first in the stack and so, on the same level, the right most node is already updated in the
            # dictionary.
            elif level == d[vertical][1]:
                pass

            # if however, a greater level is found for this vertical, then update the dictionary for this vertical.
            elif level > d[vertical][1]:
                d[vertical] = (node, level)

            # push left and right nodes respectively.
            if node.left is not None:
                stack.push((node.left, level + 1, vertical - 1))
            if node.right is not None:
                stack.push((node.right, level + 1, vertical + 1))
        for i in range(mini, maxi + 1):
            result.append(d[i][0].data)
        print(result)
        return result


# Example 1
n20, n8, n22, n5, n3, n4, n25, n10, n14, n28 = TreeNode(20), TreeNode(8), TreeNode(22), TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(25), TreeNode(10), TreeNode(14), TreeNode(28)
n20.left = n8
n20.right = n22
n8.left = n5
n8.right = n3
n3.left = n10
n22.left = n4
n22.right = n25
n4.right = n14
n25.left = n28
Solution.get_bottom_view(n20)

# Example 2
n1, n2, n3 = TreeNode(1), TreeNode(2), TreeNode(3)
n1.left = n2
n1.right = n3
Solution.get_bottom_view(n1)

# Example 3
n10, n20, n30, n40, n60 = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
Solution.get_bottom_view(n10)

# Example 4
n1, n2 = TreeNode(1), TreeNode(2)
n1.left = n2
Solution.get_bottom_view(n1)

# Example 5
n1, n2, n3, n4, n5, n6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
Solution.get_bottom_view(n1)

# Example 6
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n10
n4.right = n5
n5.right = n6
n3.left = n9
n3.right = n11
Solution.get_bottom_view(n1)

# Example 7
n2, n7, n5, n21, n6, n9, n11, n4, n51 = TreeNode(2), TreeNode(7), TreeNode(5), TreeNode(2), TreeNode(6), TreeNode(9), TreeNode(11), TreeNode(4), TreeNode(5)
n2.left = n7
n2.right = n5
n7.left = n21
n7.right = n6
n6.left = n51
n6.right = n11
n5.right = n9
n9.left = n4
Solution.get_bottom_view(n2)
