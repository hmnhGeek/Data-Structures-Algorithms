# Problem link - https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1
# Solution - https://www.youtube.com/watch?v=R6uoSjZ2imo&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=54


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
    def _dfs(graph, visited, node, stack):
        # mark the node as visited
        visited[node] = True

        # attempt DFS on adjacent nodes.
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, visited, adj_node, stack)

        # push the current node into stack.
        stack.push(node)

    @staticmethod
    def _reverse_graph(graph):
        reversed_graph = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed_graph[adj_node].append(node)
        return reversed_graph

    @staticmethod
    def _collect_strongly_connected_components(stack, visited, reversed_graph, temp_stack, strongly_connected_components):
        # while the ordered stack is not empty, i.e., not all the nodes are visited...
        while not stack.is_empty():
            # pop the node
            node = stack.pop()

            # if the node is not visited, attempt a DFS but use temp_stack this time.
            if not visited[node]:
                # since the DFS is attempted on reversed_graph, only strongly connected components will be visited
                # and store the nodes of these SCCs in temp_stack.
                Solution._dfs(reversed_graph, visited, node, temp_stack)

            # store the individual nodes from the SCC into a list.
            component = []
            while not temp_stack.is_empty():
                component.append(temp_stack.pop())

            # if the component has some nodes, push it to SCC list.
            if len(component) > 0:
                strongly_connected_components.append(component)

    @staticmethod
    def get_strongly_connected_components(graph):
        # create a stack to store the nodes in order of reachability.
        stack = Stack()

        # Will take O(V) space.
        visited = {i: False for i in graph}

        # attempt a DFS from one of the nodes and populate the stack. It will take O(V + E) time.
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, visited, node, stack)

        # reverse the graph. It will take O(V + E) time and O(V + E) space.
        reversed_graph = Solution._reverse_graph(graph)

        # restore visited array.
        visited = {i: False for i in graph}

        # create a temp_stack to store the individual SCCs.
        temp_stack = Stack()
        strongly_connected_components = []

        # collect the individual SCCs into the list and print it. This will also take O(V + E) time and O(V + E) space.
        # because its a simple DFS.
        Solution._collect_strongly_connected_components(stack, visited, reversed_graph, temp_stack, strongly_connected_components)
        print(strongly_connected_components)


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

Solution.get_strongly_connected_components(
    {
        0: [2, 3],
        1: [0],
        2: [1],
        3: [4],
        4: []
    }
)

Solution.get_strongly_connected_components(
    {
        0: [1],
        1: [2],
        2: [0]
    }
)