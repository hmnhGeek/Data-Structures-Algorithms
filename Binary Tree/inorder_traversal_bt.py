# Problem link - https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/


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


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class InorderTraversal:
    @staticmethod
    def _recursive(root: Node):
        if root is not None:
            InorderTraversal._recursive(root.left)
            print(root.data, end=" ")
            InorderTraversal._recursive(root.right)

    @staticmethod
    def recursive(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n) for the recursion stack.
        """
        InorderTraversal._recursive(root)
        print()

    @staticmethod
    def iterative(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # initialize a stack because the recursion stack is no longer there.
        stack = Stack()

        # start from the root node.
        curr = root

        # ALGORITHM
        # For a given node, go all the way to leftmost leaf node while pushing to stack.
        # While popping the current node, print it, and go top its right subtree and follow step 1 on right subtree root

        # initially, push the left border of the tree into stack
        while curr is not None:
            stack.push(curr)
            curr = curr.left

        # update stack until it gets empty.
        while not stack.is_empty():
            # pop the current node and print it.
            node = stack.pop()
            print(node.data, end=" ")

            # get the right subtree root (basically we printed left, node, and now going to right subtree)
            right_subtree = node.right

            # continuously push left boundary of this subtree into the stack.
            while right_subtree is not None:
                stack.push(right_subtree)
                right_subtree = right_subtree.left
        print()


# Example 1
n1, n2, n3, n4, n5, n6 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
n1.left = n2
n2.left = n4
n2.right = n5
n1.right = n3
n3.right = n6
InorderTraversal.iterative(n1)
InorderTraversal.recursive(n1)

print()
# Example 2
n1, n1r, n2, n2r, n4, n6, n9, n9l, n9r = Node(1), Node(1), Node(2), Node(2), Node(4), Node(6), Node(9), Node(9), Node(9)
n6.left = n9
n9.left = n9l
n9l.left = n1
n2.left = n9r
n6.right = n2
n2.right = n2r
n9.right = n1r
n9l.right = n4
InorderTraversal.iterative(n6)
InorderTraversal.recursive(n6)

print()
# Example 3
n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.left = n2
n2.left = n4
n3.left = n5
n5.left = n7
n1.right = n3
n3.right = n6
n5.right = n8
InorderTraversal.iterative(n1)
InorderTraversal.recursive(n1)