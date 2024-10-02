# Problem link - https://www.geeksforgeeks.org/problems/level-order-traversal/1


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


class LevelOrderTraversal:
    @staticmethod
    def traverse(root):
        # Time complexity is O(n) and space complexity is O(n) for the queue.
        queue = Queue()
        queue.push((root, 1))
        result = {}

        while not queue.is_empty():
            node, level = queue.pop()

            if level in result:
                result[level].append(node.data)
            else:
                result[level] = [node.data]

            if node.left is not None:
                queue.push((node.left, level + 1))
            if node.right is not None:
                queue.push((node.right, level + 1))
        return result


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


# Example 1
one, two, three = TreeNode(1), TreeNode(2), TreeNode(3)
one.left = three
one.right = two
print(LevelOrderTraversal.traverse(one))

# Example 2
ten, twty, thrty, fourty, sixty, svnty = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60), TreeNode(70)
ten.left = twty
twty.left = fourty
twty.right = sixty
ten.right = thrty
thrty.right = svnty
print(LevelOrderTraversal.traverse(ten))