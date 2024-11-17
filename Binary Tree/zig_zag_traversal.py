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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_zig_zag_traversal(root: Node):
        """
            For each level we are doing shuffling between queue and stack. Hence, time complexity is O(n^2) and space is
            O(n) because all the nodes go into either stack or queue at a time.
        """
        # create blank stack and queue.
        stack = Stack()
        queue = Queue()

        # for root node, set left to right traversal as True and push the root node in to the Queue.
        left_to_right = True
        queue.push(root)

        # run an infinite loop.
        while 1:
            # till you don't complete a level, i.e., the queue does not get empty for a single level...
            while not queue.is_empty():
                # pop the node from queue and print it.
                node = queue.pop()
                print(node.data, end=" ")

                # push the next level traversal on the stack according to left_to_right variable.
                if left_to_right:
                    if node.left is not None:
                        stack.push(node.left)
                    if node.right is not None:
                        stack.push(node.right)
                else:
                    if node.right is not None:
                        stack.push(node.right)
                    if node.left is not None:
                        stack.push(node.left)

            # empty the stack into the queue. Why? because according to left to right, say true, we pushed in stack
            # first the left nodes and then the right nodes. But this left to right equal to True was for the previous
            # level. For next level, we must reverse whatever is in stack. Also, reverse the boolean value of left to
            # right after stack gets empty (storing the correct order for next level).
            while not stack.is_empty():
                queue.push(stack.pop())
            left_to_right = not left_to_right

            # if both queue and stack got empty, there are no further nodes to traverse. Break from the infinite loop.
            if queue.is_empty() and stack.is_empty():
                print()
                break


# Example 1
n5, n1, n9, n3, n2, n8, n4 = TreeNode(5), TreeNode(1), TreeNode(9), TreeNode(3), TreeNode(2), TreeNode(8), TreeNode(4)
n5.left = n1
n5.right = n9
n1.left = n3
n1.right = n2
n9.left = n8
n9.right = n4
Solution.get_zig_zag_traversal(n5)

# Example 2
n7, n9, n71, n8, n81, n6, n10, n91 = TreeNode(7), TreeNode(9), TreeNode(7), TreeNode(8), TreeNode(8), TreeNode(6), TreeNode(10), TreeNode(9)
n7.left = n9
n7.right = n71
n9.left = n8
n9.right = n81
n71.left = n6
n8.left = n10
n8.right = n91
Solution.get_zig_zag_traversal(n7)

# Example 3
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
Solution.get_zig_zag_traversal(n1)