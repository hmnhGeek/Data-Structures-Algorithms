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
        level_order = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.pop()
            level_order.append(node.data if node != float('inf') else node)

            if node == float('inf'):
                continue

            if node.left is None and node.right is None:
                queue.enqueue(float('inf'))
                queue.enqueue(float('inf'))
                continue

            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

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
            if level_order[pi] < level_order[max_child_index]:
                self.valid_max_heap = False
                return
            self._max_heapify_down(level_order, max_child_index)

    def is_valid_max_heap(self):
        self.valid_max_heap = True
        level_order = self.get_level_order()
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