# Problem link - https://www.geeksforgeeks.org/problems/binary-tree-to-bst/1


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def _populate_inorder(self, start_node, inorder):
        if start_node:
            self._populate_inorder(start_node.left, inorder)
            inorder.append(start_node)
            self._populate_inorder(start_node.right, inorder)

    def _repopulate_tree(self, start_node, index, inorder_traversal_of_bst):
        # It is a simple inorder traversal code only. Basically what we are trying here is to traverse the binary tree
        # in inorder fashion. And while traversing, change the data of each node in it from the data of inorder
        # traversal of the BST. We must return index value to keep track of indices, otherwise the backtracking
        # approach would have reset the index back to 0. This will take O(H) recursion stack space and O(N) time.
        if start_node:
            index = self._repopulate_tree(start_node.left, index, inorder_traversal_of_bst)
            start_node.data = inorder_traversal_of_bst[index]
            # ensure to increment the index by 1 once it is utilized.
            index += 1
            index = self._repopulate_tree(start_node.right, index, inorder_traversal_of_bst)
        return index

    def _get_inorder(self):
        inorder = []
        self._populate_inorder(self.root, inorder)
        return inorder

    def convert_to_bst(self):
        # Overall time complexity is O(N * log(N)) and O(N + H) space.

        # Get the inorder traversal of the binary tree in O(N) time and O(N) space.
        inorder_traversal = self._get_inorder()

        # sort the inorder traversal to make an inorder traversal of a BST - Takes O(N * log(N)) time.
        inorder_traversal.sort(key=lambda node: node.data)

        # Create a new traversal list having only the data from the traversal nodes, because if we simply pass the
        # array `inorder_traversal` into recursion, then they are basically referencing the actual nodes from the
        # original binary tree and will also get modified while modifying the tree nodes. So, just keep the data
        # handy in a new list because that's what we actually want in the recursion tree and node the nodes themselves.
        # This will take another O(N) time.
        inorder_traversal_of_bst = [i.data for i in inorder_traversal]

        # start with the first node from the BST inorder.
        inorder_traversal_index = 0

        # start the recursion. This will take another O(N) time and O(H) space.
        self._repopulate_tree(self.root, inorder_traversal_index, inorder_traversal_of_bst)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(start.data, end=" ")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


def example1():
    one, two, three = Node(1), Node(2), Node(3)
    one.left = two
    one.right = three
    tree = BinaryTree(one)
    tree.show()
    tree.convert_to_bst()
    tree.show()


def example2():
    ten, two, four, eight, svn = Node(10), Node(2), Node(4), Node(8), Node(7)
    ten.left = two
    two.left = eight
    two.right = four
    ten.right = svn
    tree = BinaryTree(ten)
    tree.show()
    tree.convert_to_bst()
    tree.show()


def example3():
    ten, trty, fifteen, twty, five = Node(10), Node(30), Node(15), Node(20), Node(5)
    ten.left = trty
    trty.left = twty
    ten.right = fifteen
    fifteen.right = five
    tree = BinaryTree(ten)
    tree.show()
    tree.convert_to_bst()
    tree.show()


example1()

example2()

example3()