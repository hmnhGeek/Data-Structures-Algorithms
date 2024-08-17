# Problem link - https://www.geeksforgeeks.org/problems/is-binary-tree-heap/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def enqueue(self, x):
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

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class MaxHeapValidator:
    def __init__(self, tree_root: Node):
        self.root = tree_root
        self.valid_max_heap = True

    def get_level_order(self):
        # in a queue, push the root node as we are about to do a BFS traversal on this BT.
        level_order = []
        queue = Queue()
        queue.enqueue(self.root)

        # typical BFS
        while not queue.is_empty():
            node = queue.pop()

            # if the popped element is a node, store its data, otherwise it must be float('inf'); in that case simply
            # append float('inf') in level order.
            level_order.append(node.data if node != float('inf') else node)

            # if node is inf, it's a null node, having no children, continue and skip below part
            if node == float('inf'):
                continue

            # if node is a leaf node, add two inf values into queue denoting a leaf node has been inserted just before.
            # ensure to continue as nothing else after this needs to be added into the queue.
            if node.left is None and node.right is None:
                queue.enqueue(float('inf'))
                queue.enqueue(float('inf'))
                continue

            # if the node is not a leaf node, insert its left and right children into the queue respectively.
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

        # start traversing from the reverse side of level order and get the first non-inf element index. Till this
        # index is the actual level order traversal. You may ask why add inf at all when at the end we are removing
        # them. inf denote that anything after them in the level order will never be a node. However, consider this
        # example:
        """
                        97
                       /  \___
                      46      37
                     /  \     / \
                    12   3   7  31
                        / \
                       2   4
        """
        # if we don't insert inf, the level order would be 97, 46, 37, 12, 3, 7, 31, 2, 4 which is a max-heap. But it is
        # not a max heap. By inserting inf we get this [97, 46, 37, 12, inf, inf, 3, 7, 31, 2, 4, inf, ..]. At the end
        # it is expected to have inf. But not in b/w. This is because it's not a complete BT. A complete BT must have
        # left and right leaf nodes for node 12 otherwise left and right nodes must not exist for node 3.
        for i in range(-1, -len(level_order) - 1, -1):
            if level_order[i] != float('inf'):
                break
        return level_order[:i+1]

    def _get_lci(self, level_order, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(level_order)) else None

    def _get_rci(self, level_order, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(level_order)) else None

    def _get_max_child_index(self, level_order, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci

        max_child_index = lci
        if level_order[rci] > level_order[max_child_index]:
            max_child_index = rci
        return max_child_index

    def _max_heapify_down(self, level_order, pi):
        lci, rci = self._get_lci(level_order, pi), self._get_rci(level_order, pi)
        max_child_index = self._get_max_child_index(level_order, lci, rci)

        if max_child_index is not None:
            # if at any point max heap property fails, set the global valid variable to false.
            if level_order[pi] < level_order[max_child_index]:
                self.valid_max_heap = False
                return
            self._max_heapify_down(level_order, max_child_index)

    def is_valid_max_heap(self):
        # Overall time complexity is O(N) and space is also O(N).

        # assume the BT is a max heap for now.
        self.valid_max_heap = True

        # extract the level order traversal of this BT. Takes O(N) time and O(N) space (with queue also taking same).
        level_order = self.get_level_order()

        # do a max heapification downwards and at any point if heapification property fails, set global valid_max_heap
        # property to false and return it. Takes O(log(N)) time.
        self._max_heapify_down(level_order, 0)
        return self.valid_max_heap


def example1():
    two, five, three = TreeNode(2), TreeNode(5), TreeNode(3)
    five.left = two
    five.right = three
    print(MaxHeapValidator(five).is_valid_max_heap())

def example2():
    ten, twty, thirty, fourty, sixty = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60)
    ten.left = twty
    twty.left = fourty
    ten.right = thirty
    twty.right = sixty
    print(MaxHeapValidator(ten).is_valid_max_heap())


def example3():
    n97, n46, n37, n12, n3, n7, n31, n6, n9 = TreeNode(97), TreeNode(46), TreeNode(37), TreeNode(12), TreeNode(3), TreeNode(7), TreeNode(31), TreeNode(6), TreeNode(9)
    n97.left = n46
    n46.left = n12
    n12.left = n6
    n37.left = n7
    n46.right = n3
    n12.right = n9
    n37.right = n31
    print(MaxHeapValidator(n97).is_valid_max_heap())


def example4():
    n97 = TreeNode(97)
    n46 = TreeNode(46)
    n37 = TreeNode(37)
    n12 = TreeNode(12)
    n3 = TreeNode(3)
    n7 = TreeNode(7)
    n31 = TreeNode(31)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n97.left = n46
    n46.left = n12
    n37.left = n7
    n3.left = n2
    n46.right = n3
    n3.right = n4
    n97.right = n37
    n37.right = n31
    print(MaxHeapValidator(n97).is_valid_max_heap())


def example5():
    n97 = TreeNode(97)
    n46 = TreeNode(46)
    n37 = TreeNode(37)
    n12 = TreeNode(12)
    n3 = TreeNode(3)
    n7 = TreeNode(7)
    n31 = TreeNode(31)
    n97.left = n46
    n46.left = n12
    n37.left = n7
    n46.right = n3
    n97.right = n37
    n37.right = n31
    print(MaxHeapValidator(n97).is_valid_max_heap())


def example6():
    n9, n7, n5, n3, n1, n4 = TreeNode(9), TreeNode(7), TreeNode(5), TreeNode(3), TreeNode(1), TreeNode(4)
    n9.left = n7
    n7.left = n3
    n7.right = n1
    n9.right = n5
    n5.right = n4
    print(MaxHeapValidator(n9).is_valid_max_heap())


def example7():
    n40 = TreeNode(40)
    n36 = TreeNode(36)
    n23 = TreeNode(23)
    n10 = TreeNode(10)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1 = TreeNode(1)
    n14 = TreeNode(14)
    n0 = TreeNode(0)
    n40.left = n36
    n36.left = n10
    n10.left = n1
    n23.left = n5
    n5.left = n14
    n40.right = n23
    n23.right = n6
    n6.left = n0
    print(MaxHeapValidator(n40).is_valid_max_heap())


example1()
example2()
example3()
example4()
example5()
example6()
example7()