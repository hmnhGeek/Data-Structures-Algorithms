class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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
            node.next = self.head
            self.head = node
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

    def __str__(self):
        result = "["
        curr = self.head
        while curr != self.tail:
            result += f"{curr.data}, "
            curr = curr.next
        result += f"{curr.data}]"
        return result


class TopologicalSort:
    @staticmethod
    def get_topo_sort(graph):
        visited = {i: False for i in graph}
        stack = Stack()
        # result = []
        # for node in graph:
        #     if not visited[node]:
        #         # TopologicalSort._dfs(graph, node, stack)
        # # while not stack.is_empty():
