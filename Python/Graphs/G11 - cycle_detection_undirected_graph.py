# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
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


class Graph:
    @staticmethod
    def _has_cycle(graph, start_node, visited):
        # we will use BFS to perform cycle detection. The idea is that the node at which cycle is forming,
        # can be reached by two parent nodes.

        # create a queue and push the starting node with parent as None.
        queue = Queue()
        queue.push((start_node, None))

        # BFS while condition...
        while not queue.is_empty():
            # pop the node
            node, parent = queue.pop()
            # if the node is visited already, that means in there is someone else at the same level through
            # which we can reach the same node. Hence, there is a cycle. Return true.
            if visited[node]:
                return True
            # mark the node as visited.
            visited[node] = True
            # loop on the adjacent nodes of this node.
            for adj_node in graph[node]:
                # if the adjacent node is not visited, push it to queue with parent as the current node.
                if not visited[adj_node]:
                    queue.push((adj_node, node))
        # return false if BFS is completed successfully as there is no cycle.
        return False

    @staticmethod
    def has_cycle(graph):
        # create a blank visited array
        visited = {i: False for i in graph}
        # handle all the components in the graph
        for node in visited:
            if not visited[node]:
                # pass the current node as the starting node and if the component has a cycle, return True
                if Graph._has_cycle(graph, node, visited):
                    return True
        # return False as there was no cycle in any component.
        return False


print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [5],
            3: [1, 4, 6],
            4: [3],
            5: [7],
            6: [3, 7],
            7: [5, 6]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [],
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
    )
)