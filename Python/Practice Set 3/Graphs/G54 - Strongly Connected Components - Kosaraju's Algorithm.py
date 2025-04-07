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


class Solution:
    @staticmethod
    def _dfs1(graph, node, visited, stack):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs1(graph, adj_node, visited, stack)
        stack.push(node)

    @staticmethod
    def _get_topological_sort(graph):
        stack = Stack()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs1(graph, node, visited, stack)
        return stack

    @staticmethod
    def _get_reversed_graph(graph):
        reversed_graph = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                if node not in reversed_graph[adj_node]:
                    reversed_graph[adj_node].append(node)
        return reversed_graph

    @staticmethod
    def _dfs(graph, node, visited, component):
        visited[node] = True
        if node not in component:
            component.append(node)
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited, component)

    @staticmethod
    def get_strongly_connected_components(graph):
        # get a stack with the topological sort of the original graph. This will take O(V + E) time and O(V) space.
        stack = Solution._get_topological_sort(graph)

        # reverse the graph so that SCCs are isolated. This will take O(V + E) time and O(V + E) space.
        reversed_graph = Solution._get_reversed_graph(graph)

        # store the SCCs in a variable
        strongly_connected_components = []

        # create a visited array of size O(V).
        visited = {i: False for i in graph}

        # while the stack is not empty...
        while not stack.is_empty():
            # get the top node.
            node = stack.pop()

            # and if that node is not visited yet, start a DFS from it.
            if not visited[node]:
                # also populate the component and finally add it to SCCs list.
                component = []
                Solution._dfs(reversed_graph, node, visited, component)
                strongly_connected_components.append(component)

        # return the SCCs.
        return strongly_connected_components


print(
    Solution.get_strongly_connected_components(
        {
            0: [1],
            1: [2],
            2: [0, 3],
            3: [4],
            4: [5, 7],
            5: [6],
            6: [4, 7],
            7: []
        }
    )
)

print(
    Solution.get_strongly_connected_components(
        {
            0: [2, 3],
            1: [0],
            2: [1],
            3: [4],
            4: []
        }
    )
)

print(
    Solution.get_strongly_connected_components(
        {
            0: [1],
            1: [2],
            2: [0]
        }
    )
)

print(
    Solution.get_strongly_connected_components(
        {
            1: [2],
            2: [3, 4],
            3: [4, 6],
            4: [1, 5],
            5: [6],
            6: [7],
            7: [5]
        }
    )
)
