# Problem link - https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
# Solution - https://www.youtube.com/watch?v=-tgVpUgsQ5k&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=5


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
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def bfs(self, start_node):
        """
            Time complexity is O(V + E) and space complexity is O(V) for the queue.
        """

        # if the node is not there in the graph, there is no need to perform BFS.
        if start_node not in self.graph:
            return

        # initialize a queue to start BFS and push the starting node with level = 0 in the queue.
        queue = Queue()
        queue.push((start_node, 0))

        # create a blank visited array for each node
        visited = {i: False for i in self.graph}

        # create a variable to store BFS traversal
        result = {}

        # till every node is visited
        while not queue.is_empty():
            # pop the current node and its level
            node, level = queue.pop()

            # if the popped node is not visited, visit it and update it in the result.
            if not visited[node]:
                visited[node] = True

                # if witnessing this level for the first time, add this node with this level
                if level not in result:
                    result[level] = [node]
                else:
                    # else push this new node into the level
                    result[level].append(node)

            # traverse on the adjacent nodes of the current node.
            for adj_node in self.graph[node]:
                # if the adjacent node is not visited, push it to the queue with +1 level
                if not visited[adj_node]:
                    queue.push((adj_node, level + 1))
        # return the BFS traversal.
        return result


print(
    Graph(
        {
            1: [2, 6],
            2: [1, 3, 4],
            3: [2],
            4: [2, 5],
            5: [4, 7],
            6: [1, 7, 8],
            7: [5, 6],
            8: [6]
        }
    ).bfs(5)
)

print(
    Graph(
        {
            1: [2, 3],
            2: [5],
            3: [1, 4, 6],
            4: [3],
            5: [7],
            6: [3, 7],
            7: [5, 6]
        }
    ).bfs(1)
)