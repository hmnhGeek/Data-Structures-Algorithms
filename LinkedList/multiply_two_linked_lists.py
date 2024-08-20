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
    # Overall time complexity is O(m + n) and space complexity is O(1).

    # initialize num1 and num2, representing the numbers stored in the form of linked lists.
    num1, num2 = 0, 0

    # stand on the heads of both the linked lists
    curr1, curr2 = l1.head, l2.head

    # extract the number in first list
    while curr1 is not None:
        # update the number by multiplying it by 10 and adding curr's data value to the result
        num1 = num1*10 + curr1.data
        curr1 = curr1.next

    # extract the number in second list
    while curr2 is not None:
        # update the number by multiplying it by 10 and adding curr's data value to the result
        num2 = num2*10 + curr2.data
        curr2 = curr2.next

    # return the multiplied number
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


def example2():
    print("Example 2")
    l1 = LinkedList()
    l1.build([1, 2, 3])
    l2 = LinkedList()
    l2.build([5, 6])
    l1.show()
    l2.show()
    print(multiply(l1, l2))


example1()
example2()