# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
# Solution - https://www.youtube.com/watch?v=iTBaI90lpDQ&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=23


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
    def _populate_indegrees(graph, indegrees):
        for node in graph:
            for adj_node in graph[node]:
                indegrees[adj_node] += 1

    @staticmethod
    def has_cycle(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        queue = Queue()

        # get the indegrees of the nodes in O(V + E) time and O(V) space.
        indegrees = {i: 0 for i in graph}
        Solution._populate_indegrees(graph, indegrees)

        # store the count of topo sort.
        count = 0

        # push all the 0 indegree nodes into the queue.
        for i in indegrees:
            if indegrees[i] == 0:
                queue.push(i)

        # typical topo sort condition
        while not queue.is_empty():
            # pop the node and increment the count
            node = queue.pop()
            count += 1
            # loop on the adjacent nodes
            for adj_node in graph[node]:
                # and decrement the degree of adjacent nodes
                indegrees[adj_node] -= 1
                # if the adjacent node is disconnected, push the adj_node into queue.
                if indegrees[adj_node] == 0:
                    queue.push(adj_node)
        # return no cycle if topo sort length is same as graph length else return has cycle.
        return count != len(graph)


print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2],
            2: [3],
            3: [3]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1],
            1: [2],
            2: []
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [0, 3],
            3: [3]
        }
    )
)

print(
    Solution.has_cycle(
        {
            0: [1, 2],
            1: [2],
            2: [3],
            3: []
        }
    )
)