class Utility:
    def __init__(self):
        pass

    @staticmethod
    def counter(iterable):
        result = {}
        for i in iterable:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        return result


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def get_level_order(self):
        queue = Queue()
        if self.root is not None:
            queue.push((self.root, 0))
        level_order_traversal = {}

        while not queue.is_empty():
            node, level = queue.pop()
            if level not in level_order_traversal:
                level_order_traversal[level] = [node.data]
            else:
                level_order_traversal[level].append(node.data)

            if node.left is not None:
                queue.push((node.left, level + 1))
            if node.right is not None:
                queue.push((node.right, level + 1))
        return level_order_traversal


def are_anagrams(tree1: BinaryTree, tree2: BinaryTree) -> bool:
    level_order_1 = tree1.get_level_order()
    level_order_2 = tree2.get_level_order()

    if len(level_order_1) != len(level_order_2):
        return False

    for level in level_order_1:
        nodes1 = level_order_1[level]
        nodes2 = level_order_2[level]
        if Utility.counter(nodes1) != Utility.counter(nodes2):
            return False
    return True


# Example 1
one, two, three, four, five = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
one.left = three
two.left = five
one.right = two
two.right = four
tree = BinaryTree(one)
print(tree.get_level_order())

one1, two2, three3, four4, five5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
one1.left = two2
two2.left = four4
one1.right = three3
two2.right = five5
tree2 = BinaryTree(one1)
print(tree2.get_level_order())
print(are_anagrams(tree, tree2))

print()

# Example 2
one, two, three, four, five = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
one1, two2, three3, four4, five5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
one.left = two
two.left = five
one.right = three
two.right = four
one1.left = two2
two2.left = five5
one1.right = four4
two2.right = three3
t1 = BinaryTree(one)
t2 = BinaryTree(one1)
print(t1.get_level_order())
print(t2.get_level_order())
print(are_anagrams(t1, t2))