class Node:
    def __init__(self, data):
        self.data = data
        self.child = self.next = None


class Solution:
    @staticmethod
    def merge(h1, h2):
        dummy = Node(None)
        temp = dummy
        while h1 is not None and h2 is not None:
            if h1.data <= h2.data:
                temp.child = h1
                temp = h1
                h1.next = None
                h1 = h1.child
            else:
                temp.child = h2
                temp = h2
                h2.next = None
                h2 = h2.child
        while h1 is not None:
            temp.child = h1
            temp = h1
            h1.next = None
            h1 = h1.child
        while h2 is not None:
            temp.child = h2
            temp = h2
            h2.next = None
            h2 = h2.child
        return dummy.child

    @staticmethod
    def flatten(start_node: Node):
        if start_node is None or start_node.next is None:
            return start_node
        merged_head = Solution.flatten(start_node.next)
        return Solution.merge(start_node, merged_head)

    @staticmethod
    def show(start_node):
        curr = start_node
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.child
        print()


# Example 1
n5 = Node(5)
n7 = Node(7)
n8 = Node(8)
n30 = Node(30)
n10 = Node(10)
n19 = Node(19)
n22 = Node(22)
n50 = Node(50)
n28 = Node(28)
n5.next = n10
n10.next = n19
n19.next = n28
n5.child = n7
n7.child = n8
n8.child = n30
n19.child = n22
n22.child = n50
head = Solution.flatten(n5)
Solution.show(head)


