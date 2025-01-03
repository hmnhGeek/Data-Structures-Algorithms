# Problem link - https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
# Solution - https://www.youtube.com/watch?v=BPlrALf1LDU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=11


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
    def _has_cycle(graph, source, visited):
        # create a new queue and push the starting node
        queue = Queue()
        queue.push(source)

        # typical BFS...
        while not queue.is_empty():
            node = queue.pop()

            # if the popped node is already visited, return True, which means there's a cycle.
            if visited[node]:
                return True

            # mark the popped node as visited.
            visited[node] = True

            # loop on the adjacent nodes of this node and if they are not visited, push them to the queue.
            for adj_node in graph[node]:
                if not visited[adj_node]:
                    queue.push(adj_node)

        # if queue got empty, there was no cycle, return False.
        return False

    @staticmethod
    def detect_cycle(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # create a visited dictionary in O(V) space.
        visited = {i: False for i in graph}
        for node in graph:
            # if a component is detected and its start node is not visited, initiate a BFS
            if not visited[node]:
                if Solution._has_cycle(graph, node, visited):
                    # if cycle is detected, return True
                    return True
        # else, even after traversing all the nodes, if no cycle was found in any of the component, return False.
        return False


print(
    Solution.detect_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 6],
            4: [3],
            5: [2, 7],
            6: [3, 7],
            7: [5, 6]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 6],
            4: [3],
            5: [2, 7],
            6: [3],
            7: [5]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [],
            1: [2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Solution.detect_cycle(
        {
            0: [1],
            1: [0, 2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 3]
        }
    )
)