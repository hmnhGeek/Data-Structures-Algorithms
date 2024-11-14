class StackNode:
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
        node = StackNode(x)
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


class PreorderTraversal:
    def __init__(self, root: TreeNode):
        self.root = root

    def iterative(self):
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            node = stack.pop()
            print(node.data, end=" ")
            if node.right is not None:
                stack.push(node.right)
            if node.left is not None:
                stack.push(node.left)
        print()



# Example 1
n1, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)
n1.left = n2
n2.left = n4
n2.right = n5
n5.left = n8
n1.right = n3
n3.left = n6
n3.right = n9
n6.right = n7
obj1 = PreorderTraversal(n1)
obj1.iterative()