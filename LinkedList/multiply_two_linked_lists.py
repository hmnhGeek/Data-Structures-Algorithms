class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def build(self, _list):
        for i in _list:
            self.push(i)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def multiply(l1: LinkedList, l2: LinkedList) -> int:
    num1, num2 = 0, 0
    curr1, curr2 = l1.head, l2.head

    while curr1 is not None:
        num1 = num1*10 + curr1.data
        curr1 = curr1.next

    while curr2 is not None:
        num2 = num2*10 + curr2.data
        curr2 = curr2.next

    return num1*num2


def example1():
    print("Example 1")
    l1 = LinkedList()
    l1.build([9, 4, 6])
    l2 = LinkedList()
    l2.build([8, 4])
    l1.show()
    l2.show()
    print(multiply(l1, l2))

example1()