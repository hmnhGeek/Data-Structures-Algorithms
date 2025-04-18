# Problem link - https://www.geeksforgeeks.org/problems/reverse-level-order-traversal/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Queue:
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


class Solution:
    @staticmethod
    def reverse_level_order(root: TreeNode):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # define a queue and push the root node into it.
        queue = Queue()
        queue.push(root)

        # define a level order list
        level_order = []

        # while the queue is not empty...
        while not queue.is_empty():
            # pop the current node.
            node = queue.pop()

            # append the node's data
            level_order.append(node.data)

            # first push right node and then left into the queue.
            if node.right is not None:
                queue.push(node.right)
            if node.left is not None:
                queue.push(node.left)

        # return the reverse of the level order list as the final answer.
        return level_order[-1:-len(level_order)-1:-1]


# Example 1
one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
one.left = two
one.right = three
print(Solution.reverse_level_order(one))

# Example 2
ten, twenty, thirty, fourty, sixty = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60)
ten.left = twenty
twenty.left = fourty
ten.right = thirty
twenty.right = sixty
print(Solution.reverse_level_order(ten))
