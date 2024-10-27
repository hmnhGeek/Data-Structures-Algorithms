# Problem link - https://www.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1


class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.left = self.right = None
        self.size = 1
        self.ht = 1
        self.d = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

    def recalc_aug(self, parent: Node):
        self.d = 0
        while parent is not None:
            left_sz, right_sz = parent.left.size if parent.left else 0, parent.right.size if parent.right else 0
            left_ht, right_ht = parent.left.ht if parent.left else 0, parent.right.ht if parent.right else 0
            parent.size = 1 + left_sz + right_sz
            parent.ht = 1 + max(left_ht, right_ht)
            parent.d = 1 + left_ht + right_ht
            self.d = max(self.d, parent.d)
            parent = parent.parent

    def _insert(self, start: Node, node: Node):
        if start is None or node is None:
            return
        if node.data >= start.data:
            if start.right is not None:
                return self._insert(start.right, node)
            start.right = node
            node.parent = start
            self.recalc_aug(start)
            return
        if start.left is not None:
            return self._insert(start.left, node)
        start.left = node
        node.parent = start
        self.recalc_aug(start)
        return

    def insert(self, x: int):
        node = Node(x)
        if self.root is None:
            self.root = node
            self.d = 1
            return
        return self._insert(self.root, node)

    def get_leftmost_leaf(self, node: Node):
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node

    def get_rightmost_leaf(self, node: Node):
        if node is None:
            return
        while node.right is not None:
            node = node.right
        return node

    def get_successor(self, node: Node):
        if node is None:
            return
        if node.right is not None:
            return self.get_leftmost_leaf(node.right)
        parent = node.parent
        if parent is None:
            return
        while parent.left != node:
            node = node.parent
            parent = parent.parent
            if parent is None:
                return
        return parent

    def get_predecessor(self, node: Node):
        if node is None:
            return
        if node.left is not None:
            return self.get_rightmost_leaf(node.left)
        parent = node.parent
        if parent is None:
            return
        while parent.right != node:
            node = node.parent
            parent = parent.parent
            if parent is None:
                return
        return parent

    def _delete(self, node: Node):
        if node is None:
            return
        if node.left is None and node.right is None:
            parent = node.parent
            if parent is not None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
                self.d = 0
            self.recalc_aug(parent)
            del node
            return
        if node.right is not None:
            successor = self.get_successor(node)
            successor.data, node.data = node.data, successor.data
            return self._delete(successor)
        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        return self._delete(predecessor)

    def get_node(self, start: Node, data: int):
        if start is None or data is None:
            return
        if start.data == data:
            return start
        if data >= start.data:
            return self.get_node(start.right, data)
        return self.get_node(start.left, data)

    def delete(self, x: int):
        node = self.get_node(self.root, x)
        if node is not None:
            return self._delete(node)

    def _show(self, start: Node):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)


class DeadEndFinder:
    @staticmethod
    def _get_inorder(start: Node, inorder):
        if start:
            DeadEndFinder._get_inorder(start.left, inorder)
            inorder.append(start)
            DeadEndFinder._get_inorder(start.right, inorder)

    @staticmethod
    def get_inorder(bst: BinarySearchTree):
        inorder = []
        DeadEndFinder._get_inorder(bst.root, inorder)
        return inorder

    @staticmethod
    def _is_leaf(node: Node):
        return node.left is None and node.right is None

    @staticmethod
    def find_dead_end_nodes(bst: BinarySearchTree):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # get the inorder traversal of the tree in O(n) time and O(n) space.
        inorder = DeadEndFinder.get_inorder(bst)
        result = []

        # if the tree does not contain any node or only has one node, there is no dead end.
        if len(inorder) <= 1:
            return result
        
        # Specially check for the first node in the inorder traversal, i.e. the left most node in the tree.
        leftmost_node = inorder[0]
        
        # if the leftmost node has data = 1 and the difference between next node and itself is <= 1, and it is also a
        # leaf node, then nothing can be inserted between leftmost node and its next node. Plus we can't insert anything
        # before 1 as only natural numbers are allowed. Hence, this leftmost node is a dead end.
        if leftmost_node.data == 1 and inorder[1].data - leftmost_node.data <= 1 and DeadEndFinder._is_leaf(leftmost_node):
            result.append(leftmost_node.data)

        # loop on the inorder traversal from the first node till the second last node (O(n) time).
        for i in range(1, len(inorder) - 1):
            # get the current node
            node = inorder[i]

            # if the difference between the node and its predecessor and respectively with its successor is <= 1 and
            # this node is a leaf node, then this node is a dead end. Add this node into result list.
            if inorder[i + 1].data - node.data <= 1 and node.data - inorder[i - 1].data <= 1 and DeadEndFinder._is_leaf(node):
                result.append(node.data)
        # return the result list.
        return result


# Example 1
t1 = BinarySearchTree()
for i in [8, 5, 9, 2, 7, 1]:
    t1.insert(i)
print(DeadEndFinder.find_dead_end_nodes(t1))

# Example 2
t2 = BinarySearchTree()
for i in [8, 7, 10, 2, 9, 13]:
    t2.insert(i)
print(DeadEndFinder.find_dead_end_nodes(t2))

# Example 3
t3 = BinarySearchTree()
for i in [10, 6, 12, 2, 8, 11, 15]:
    t3.insert(i)
print(DeadEndFinder.find_dead_end_nodes(t3))

# Example 4
t4 = BinarySearchTree()
for i in [7, 4, 8]:
    t4.insert(i)
print(DeadEndFinder.find_dead_end_nodes(t4))
