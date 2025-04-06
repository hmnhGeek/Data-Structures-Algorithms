# Problem link - https://www.geeksforgeeks.org/problems/level-order-traversal/1


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


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

class Solution:
    @staticmethod
    def get_level_order_traversal(root: Node):
        level_order_traversal = {}
        if root is None:
            return level_order_traversal
        queue = Queue()
        queue.push((root, 0))
        while not queue.is_empty():
            node, level = queue.pop()
            if level not in level_order_traversal:
                level_order_traversal[level] = [node.data,]
            else:
                level_order_traversal[level].append(node.data)
            if node.left is not None:
                queue.push((node.left, level + 1))
            if node.right is not None:
                queue.push((node.right, level + 1))
        return level_order_traversal
    

# Example 1
one, two, three = Node(1), Node(2), Node(3)
one.left = three
one.right = two
print(Solution.get_level_order_traversal(one))

# Example 2
ten, twty, thrty, fourty, sixty, svnty = Node(10), Node(20), Node(30), Node(40), Node(60), Node(70)
ten.left = twty
twty.left = fourty
twty.right = sixty
ten.right = thrty
thrty.right = svnty
print(Solution.get_level_order_traversal(ten))

# Example 3
n1, n2, n3, n4, n5 = Node(10), Node(20), Node(30), Node(40), Node(50)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
print(Solution.get_level_order_traversal(n1))

# Example 4
n1, n2, n3, n4, n5, n6 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
n1.left = n3
n1.right = n2
n2.right = n4
n4.left = n6
n4.right = n5
print(Solution.get_level_order_traversal(n1))
