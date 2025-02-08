class Node:
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
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def get_page_faults(arr, cap):
        queue = []
        page_faults = 0
        n = len(arr)
        for i in range(n):
            if len(queue) < cap:
                if arr[i] not in queue:
                    queue.append(arr[i])
                    page_faults += 1
                else:
                    idx = queue.index(arr[i])
                    queue[idx], queue[-1] = queue[-1], queue[idx]
            elif arr[i] not in queue:
                queue.pop(0)
                queue.append(arr[i])
                page_faults += 1
            else:
                idx = queue.index(arr[i])
                queue[idx], queue[-1] = queue[-1], queue[idx]
        return page_faults


print(Solution.get_page_faults([5, 0, 1, 3, 2, 4, 1, 0, 5], 4))