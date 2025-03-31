# Problem link - https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
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

    def enqueue(self, x):
        node = Node(x)

        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


def get_min_multiplications(arr, start, end):
    # Time complexity is O(10**5 * len(arr)) and space is O(10**5)
    queue = Queue()
    queue.enqueue((start, 0))
    distances = {i: float("inf") for i in range(10**5)}

    # Typical BFS using a queue.
    while not queue.is_empty():
        num, steps = queue.dequeue()

        for i in arr:
            adj = (num*i) % 10**5

            if distances[adj] > steps + 1:
                distances[adj] = steps + 1
                if adj == end:
                    return steps + 1
                queue.enqueue((adj, steps + 1))

    return -1


print(
    get_min_multiplications(
        [2, 5, 7],
        3,
        30
    )
)

print(
    get_min_multiplications(
        [3, 4, 65],
        7,
        66175
    )
)