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
        self.head = self.head.next
        node = self.head
        del node
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def detect_cycle(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # get the source node from the graph
        source = list(graph.keys())[0]

        # get the visited array
        visited = {i: False for i in graph}

        # push the source node with parent None into the queue.
        queue = Queue()
        queue.push((source, None))

        # mark the source node as visited.
        visited[source] = True

        # typical BFS
        while not queue.is_empty():
            # get the current node and its parent.
            node, parent = queue.pop()

            # loop in the adjacent nodes...
            for adj_node in graph[node]:
                # if its parent node, continue, nothing needs to be done.
                if adj_node == parent:
                    continue

                # else if the adjacent node is not visited, push it into the queue.
                elif not visited[adj_node]:
                    visited[adj_node] = True
                    queue.push((adj_node, node))

                else:
                    # else if it's not parent, and it is already visited, then there's a cycle.
                    return True

        # if queue gets empty, there is no cycle, return False.
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
