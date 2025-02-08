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

    def get_node(self, x):
        curr = self.head
        while curr is not None:
            if curr.data == x:
                return curr
            curr = curr.next
        return None

    def swap(self, n1, n2):
        temp = n1.data
        n1.data = n2.data
        n2.data = temp

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        self.head = self.head.next
        self.length -= 1
        return item

    def __len__(self):
        return self.length


class Solution:
    @staticmethod
    def get_page_faults(arr, cap):
        queue = LinkedList()
        page_faults = 0
        n = len(arr)
        for i in range(n):
            node = queue.get_node(arr[i])
            if len(queue) < cap:
                if node is None:
                    queue.push(arr[i])
                    page_faults += 1
                else:
                    tail = queue.tail
                    queue.swap(node, tail)
            elif node is None:
                queue.pop_front()
                queue.push(arr[i])
                page_faults += 1
            else:
                node = queue.get_node(arr[i])
                tail = queue.tail
                queue.swap(node, tail)
        return page_faults


print(Solution.get_page_faults([5, 0, 1, 3, 2, 4, 1, 0, 5], 4))