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
    def get_min(start, arr, end):
        """
            Time complexity is O(10**5 * n) and space complexity is O(10**5), where n is the size of array.
        """

        # define distances for all 10**5 nodes and mark source node distance as 0.
        distances = {i: 1e6 for i in range(10**5)}
        distances[start] = 0

        # define a queue and push the start node.
        queue = Queue()
        queue.push((distances[start], start))

        # typical Dijkstra
        while not queue.is_empty():
            distance, node = queue.pop()
            for i in arr:
                # get the next node
                next_node = (i * node) % 10**5
                # and if the distance of the next node is larger than distance + 1, update the variable and push the
                # next node into the queue.
                if distances[next_node] > distance + 1:
                    distances[next_node] = distance + 1
                    queue.push((distances[next_node], next_node))

                # we could wait for the queue to get empty, but since the operations are large, we can return as soon
                # as we find the end node.
                if next_node == end:
                    return distances[next_node]

        # return -1 if end node was not found.
        return -1


print(Solution.get_min(3, [2, 5, 7], 30))
print(Solution.get_min(7, [3, 4, 65], 66175))