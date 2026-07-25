class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.bottom = None


class Solution:
    @staticmethod
    def show(head: Node):
        result = "["
        while head.bottom is not None:
            result += f"{head.data}, "
            head = head.bottom
        result += f"{head.data}]"
        print(result)

    @staticmethod
    def flatten(head: Node) -> Node:
        if head.next is None:
            return head
        flattened_head = Solution.flatten(head.next)
        return Solution._merge(head, flattened_head)

    @staticmethod
    def _merge(head: Node, fh: Node) -> Node:
        c1 = head
        c2 = fh
        dummy = Node(None)
        temp = dummy
        while c1 is not None and c2 is not None:
            if c1.data <= c2.data:
                temp.bottom = c1
                temp = c1
                c1 = c1.bottom
            else:
                temp.bottom = c2
                temp = c2
                c2 = c2.bottom
        while c1 is not None:
            temp.bottom = c1
            temp = c1
            c1 = c1.bottom
        while c2 is not None:
            temp.bottom = c2
            temp = c2
            c2 = c2.bottom
        return dummy.bottom


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
n5.bottom = n7
n7.bottom = n8
n8.bottom = n30
n19.bottom = n22
n22.bottom = n50
head = Solution.flatten(n5)
Solution.show(head)

# Example 2
n5 = Node(5)
n7 = Node(7)
n8 = Node(8)
n30 = Node(30)
n10 = Node(10)
n19 = Node(19)
n22 = Node(22)
n50 = Node(50)
n28 = Node(28)
n35 = Node(35)
n40 = Node(40)
n45 = Node(45)
n20 = Node(20)
n5.next = n10
n10.bottom = n20
n10.next = n19
n19.next = n28
n5.bottom = n7
n7.bottom = n8
n8.bottom = n30
n19.bottom = n22
n22.bottom = n50
n28.bottom = n35
n35.bottom = n40
n40.bottom = n45
head = Solution.flatten(n5)
Solution.show(head)