class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Utility:
    @staticmethod
    def is_complete_tree(root: TreeNode):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # push the root node into the queue.
        queue = Queue()
        queue.push(root)

        # store if a null node has been found or not yet.
        found_null = False

        # typical BFS.
        while not queue.is_empty():
            # pop the current node from the queue.
            node = queue.pop()

            # if the node is null, set null found to be true.
            if node is None:
                found_null = True
            else:
                # if the popped node is not null, but a null node has been found previously, then the tree is not a
                # complete binary tree.
                if found_null:
                    return False

                # else push left and right children, even if they are null.
                queue.push(node.left)
                queue.push(node.right)
        return True


class Solution:
    @staticmethod
    def _check_max_heap_property(root: TreeNode) -> bool:
        """
            Time complexity is O(n) and space complexity is O(h).
        """

        # null node should return True.
        if root is None:
            return True

        # check if root node is greater or equal to it children nodes.
        if root.left and root.data < root.left.data:
            return False
        if root.right and root.data < root.right.data:
            return False

        # recursively check for left and right subtrees.
        return Solution._check_max_heap_property(root.left) and Solution._check_max_heap_property(root.right)

    @staticmethod
    def validate_if_max_heap(root: TreeNode) -> bool:
        """
            Overall time complexity is O(n) and space complexity is O(n + h).
        """

        complete = Utility.is_complete_tree(root)
        if not complete:
            return False
        return Solution._check_max_heap_property(root)


# Example 1
n10, n20, n30, n40, n60 = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
print(Solution.validate_if_max_heap(n10))


# Example 2
n5, n2, n3 = TreeNode(5), TreeNode(2), TreeNode(3)
n5.left = n2
n5.right = n3
print(Solution.validate_if_max_heap(n5))


# Example 3
n40 = TreeNode(40)
n36 = TreeNode(36)
n23 = TreeNode(23)
n10 = TreeNode(10)
n23_1 = TreeNode(23)
n5 = TreeNode(5)
n6 = TreeNode(6)
n1 = TreeNode(1)
n14 = TreeNode(14)
n40.left = n36
n40.right = n23
n36.left = n10
n36.right = n23_1
n23.left = n5
n23.right = n6
n10.left = n1
n10.right = n14
print(Solution.validate_if_max_heap(n40))


# Example 4
n40 = TreeNode(40)
n36 = TreeNode(36)
n23 = TreeNode(23)
n10 = TreeNode(10)
n5 = TreeNode(5)
n6 = TreeNode(6)
n1 = TreeNode(1)
n14 = TreeNode(14)
n40.left = n36
n40.right = n23
n36.left = n10
n23.left = n5
n23.right = n6
n10.left = n1
n5.left = n14
print(Solution.validate_if_max_heap(n40))


# Example 5
n15 = TreeNode(15)
n14 = TreeNode(14)
n10 = TreeNode(10)
n4 = TreeNode(4)
n5 = TreeNode(5)
n11 = TreeNode(11)
n5_1 = TreeNode(5)
n1 = TreeNode(1)
n2 = TreeNode(2)
n15.left = n14
n15.right = n10
n14.left = n4
n14.right = n5
n10.left = n11
n10.right = n5
n4.left = n1
n4.right = n2
print(Solution.validate_if_max_heap(n15))
