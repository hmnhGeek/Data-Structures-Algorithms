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
    def are_anagrams(root1: Node, root2: Node) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None:
            return False
        if root2 is None:
            return False
        queue1 = Queue()
        queue2 = Queue()
        queue1.push(root1)
        queue2.push(root2)
        while not queue1.is_empty() and not queue2.is_empty():
            node1, node2 = queue1.pop(), queue2.pop()
            if node1.data != node2.data:
                return False

            if node1.left and node2.right:
                if node1.left.data == node2.right.data:
                    queue1.push(node1.left)
                    queue2.push(node2.right)
                else:
                    return False
            elif node1.left:
                return False
            elif node2.right:
                return False

            if node1.right and node2.left:
                if node1.right.data == node2.left.data:
                    queue1.push(node1.right)
                    queue2.push(node2.left)
                else:
                    return False
            elif node1.right:
                return False
            elif node2.left:
                return False

        return queue1.is_empty() and queue2.is_empty()


# Example 1
n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
n1.left = n3
n1.right = n2
n2.left = n5
n2.right = n4

m1, m2, m3, m4, m5 = Node(1), Node(2), Node(3), Node(4), Node(5)
m1.left = m2
m1.right = m3
m2.left = m4
m2.right = m5
print(Solution.are_anagrams(n1, m1))


# Example 2
one, two, three, four, five = Node(1), Node(2), Node(3), Node(4), Node(5)
one.left = two
two.left = five
one.right = three
two.right = four

one1, two1, three1, four1, five1 = Node(1), Node(2), Node(3), Node(4), Node(5)
one1.left = two1
two1.left = five1
one1.right = four1
two1.right = three1

print(Solution.are_anagrams(one, one1))
