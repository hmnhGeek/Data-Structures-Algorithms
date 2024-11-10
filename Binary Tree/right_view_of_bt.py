class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = QueueNode(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
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
    def get_right_view_of_a_binary_tree(root: TreeNode):
        level = 0
        queue = Queue()
        queue.push((root, level))
        while not queue.is_empty():
            node, node_level = queue.pop()
            if level == node_level:
                print(node.data, end=" ")
                level += 1
            if node.right is not None:
                queue.push((node.right, node_level + 1))
            if node.left is not None:
                queue.push((node.left, node_level + 1))
        print()


# Example 1
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n1.left = n2
n2.left = n4
n3.left = n6
n1.right = n3
n3.right = n7
n2.right = n5
n4.right = n8
Solution.get_right_view_of_a_binary_tree(n1)


# Example 2
n1, n2, n3 = TreeNode(1), TreeNode(2), TreeNode(3)
n1.left = n3
n1.right = n2
Solution.get_right_view_of_a_binary_tree(n1)


# Example 3
n10 = TreeNode(10)
n20 = TreeNode(20)
n30 = TreeNode(30)
n40 = TreeNode(40)
n60 = TreeNode(60)
n10.left = n20
n20.left = n40
n10.right = n30
n20.right = n60
Solution.get_right_view_of_a_binary_tree(n10)