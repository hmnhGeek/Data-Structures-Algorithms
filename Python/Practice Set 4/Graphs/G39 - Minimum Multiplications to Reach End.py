# Problem link - https://www.geeksforgeeks.org/minimum-steps-to-reach-end-from-start-by-performing-multiplication-and-mod-operations-with-array-elements/
# Solution - https://www.youtube.com/watch?v=_BvEJ3VIDWw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=39


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
    def get_min_multiplications(start, multipliers, end):
        """
            Time complexity is O(10**5 * n) and space complexity is O(10**5), where n is the size of array.
        """
        START, END = 1, 10**5
        if not (start in range(START, END + 1) and end in range(START, END + 1)):
            return
        distances = {i: 1e6 for i in range(START, END + 1)}
        distances[start] = 0
        queue = Queue()
        queue.push((distances[start], start % END))
        while not queue.is_empty():
            d, n = queue.pop()
            if n == end:
                return d
            for mul in multipliers:
                next_node = (mul * n) % END
                if distances[next_node] > d + 1:
                    distances[next_node] = d + 1
                    queue.push((d + 1, next_node))
        return distances[end]


print(Solution.get_min_multiplications(3, [2, 5, 7], 30))
print(Solution.get_min_multiplications(7, [3, 4, 65], 66175))
