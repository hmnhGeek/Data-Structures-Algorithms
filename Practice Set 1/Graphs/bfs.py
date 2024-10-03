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
        if start_node not in self.graph:
            return
        queue = Queue()
        queue.push((start_node, 0))
        visited = {i: False for i in self.graph}
        result = {}
        while not queue.is_empty():
            node, level = queue.pop()

            if not visited[node]:
                visited[node] = True
                if level not in result:
                    result[level] = [node]
                else:
                    result[level].append(node)

            for adj_node in self.graph[node]:
                if not visited[adj_node]:
                    queue.push((adj_node, level + 1))
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