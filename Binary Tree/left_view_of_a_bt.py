# Problem link - https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1
# Solution - https://www.youtube.com/watch?v=KV4mRzTjlAk&t=497s


class Node:
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
        self.left = self.right = None
        self.data = data


class LeftView:
    @staticmethod
    def _solve(root: TreeNode, level: int, queue: Queue):
        # if the root node is None, end the recursion.
        if root is None:
            return

        # if the length of the queue is same as the level value, this is the first node in the level, add it.
        if queue.length == level:
            queue.push(root.data)

        # recursively solve for left and right subtrees. Left first because we want left view.
        LeftView._solve(root.left, level + 1, queue)
        LeftView._solve(root.right, level + 1, queue)

    @staticmethod
    def get_recursive_view(root: TreeNode):
        """
            Time complexity is O(n) and space complexity is O(h).
        """

        queue = Queue()

        # start with the root node and pass down the initialized queue.
        LeftView._solve(root, 0, queue)

        # print the left view.
        while not queue.is_empty():
            print(queue.pop(), end=" ")
        print()

    @staticmethod
    def get_iterative_view(root: TreeNode):
        """
            Time complexity is O(n) and space complexity is O(max_nodes_in_level).
        """

        queue = Queue()

        # push the root node with level 0.
        queue.push((root, 0))

        # initialize a result queue also.
        result = Queue()

        # typical BFS...
        while not queue.is_empty():
            node, level = queue.pop()

            # if the result queue's length is same as that of level value, then `node` is first node to be encountered
            # on this level; add it to the result queue.
            if result.length == level:
                result.push(node.data)

            # check for left and right subtrees just like in recursion.
            if node.left is not None:
                queue.push((node.left, level + 1))
            if node.right is not None:
                queue.push((node.right, level + 1))

        # print the left view.
        while not result.is_empty():
            print(result.pop(), end=" ")
        print()

# Example 1
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n1.left = n2
n2.left = n4
n5.left = n6
n1.right = n3
n3.right = n7
n2.right = n5
LeftView.get_recursive_view(n1)
LeftView.get_iterative_view(n1)

print()
# Example 2
n1, n2, n3, n4, n5, n6, n7, n8 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8)
n1.left = n2
n2.left = n4
n4.right = n8
n2.right = n5
n1.right = n3
n3.left = n6
n3.right = n7
LeftView.get_recursive_view(n1)
LeftView.get_iterative_view(n1)