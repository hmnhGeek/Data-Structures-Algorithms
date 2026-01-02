class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def build(self, *args):
        for i in args:
            self.push(i)

    def get_middle_node(self):
        if self.length == 0:
            return
        slow = self.head
        fast = self.head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self):
        if self.is_empty() or self.length == 1:
            return
        prev, curr = None, self.head
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head, self.tail = self.tail, self.head

    def __str__(self):
        if self.is_empty():
            return "[]"
        curr = self.head
        result = "["
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{curr.data}]"
        return result


class Solution:
    @staticmethod
    def check_palindrome(l: LinkedList) -> bool:
        if l.length == 0 or l.length == 1:
            return True
        middle_node = l.get_middle_node()
        next_to_middle = middle_node.next
        middle_node.next = None
        sub_list = LinkedList()
        sub_list.head = next_to_middle
        sub_list.tail = l.tail
        sub_list.length = l.length // 2
        sub_list.reverse()
        middle_node.next = sub_list.head
        l.tail = sub_list.tail
        i, j = l.head, sub_list.head
        is_palindrome = True
        print("Partly reversed list: ", l)
        while j is not None:
            if i.data != j.data:
                is_palindrome = False
                break
            i = i.next
            j = j.next
        middle_node.next = None
        sub_list.reverse()
        middle_node.next = sub_list.head
        l.tail = sub_list.tail
        print("Restored list: ", l)
        return is_palindrome


def test(*args):
    l = LinkedList()
    l.build(*args)
    print(Solution.check_palindrome(l))
    print()


test(1, 2, 2, 1)
test(1, 2, 3, 4)
test(1, 2, 3, 2, 1)
test(1, 2, 3, 4, 1)
test(1, 2, 1, 1, 2, 1)
