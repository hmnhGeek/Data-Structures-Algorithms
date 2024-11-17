class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def push(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get_middle_node(self):
        if self.head is None:
            return
        slow = self.head
        fast = self.head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" --> ")
            curr = curr.next
        print()

    def build(self, *args):
        for i in args:
            self.push(i)


