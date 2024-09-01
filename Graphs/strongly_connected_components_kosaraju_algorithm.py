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
        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def _dfs(self, graph, node, visited, stack):
        visited[node] = True

        for adj_node in graph[node]:
            if not visited[adj_node]:
                self._dfs(graph, adj_node, visited, stack)

        stack.push(node)

    def _reverse(self):
        # Reversing the graph will take O(V + E) time and O(V + E) space for storing this graph separately.
        reversed_graph = {}
        for node in self.graph:
            for adj_node in self.graph[node]:
                if adj_node not in reversed_graph:
                    reversed_graph[adj_node] = [node]
                else:
                    reversed_graph[adj_node].append(node)

        # it could be possible that certain nodes are missing in the reversed graph, add them from the original graph.
        for node in self.graph:
            if node not in reversed_graph:
                reversed_graph[node] = []

        return reversed_graph

    def _get_topological_order(self, source_node):
        # This is the standard DFS topological sort algorithm which will take O(V + E) time and O(V) space.
        stack = Stack()
        if source_node not in self.graph:
            return stack

        visited = {i: False for i in self.graph}
        if not visited[source_node]:
            self._dfs(self.graph, source_node, visited, stack)

        return stack

    def get_strongly_connected_components(self, source):
        """
            Overall time complexity is O(V + E) and overall space complexity is O(V + E).
        """

        # get topological sorted stack in O(V + E) time and O(V) space.
        ordered_stack = self._get_topological_order(source)

        # get the reversed version of the graph in O(V + E) time and space each.
        reversed_graph = self._reverse()

        # let's start the dfs traversal on the nodes stored in stack
        visited = {i: False for i in self.graph}
        strongly_connected_components = []

        # run this loop till the stack is not empty. This will run for O(V + E) time with O(V) space
        while not ordered_stack.is_empty():
            node = ordered_stack.pop()

            # if the popped node is not visited
            if not visited[node]:
                # do a dfs traversal starting on this node and populate a local stack (on the reversed graph)
                component_stack = Stack()
                self._dfs(reversed_graph, node, visited, component_stack)
                component = []

                # pop from this local stack until you have all the nodes handy within this component.
                while not component_stack.is_empty():
                    component.append(component_stack.pop())

                # once the component is populated, add it to strongly connected components list.
                strongly_connected_components.append(component)

        # finally, return the strongly connected components.
        return strongly_connected_components


print(
    Graph(
        {
            0: [2, 3],
            1: [0],
            2: [1],
            3: [4],
            4: []
        }
    ).get_strongly_connected_components(0)
)

print(
    Graph(
        {
            0: [1],
            1: [2],
            2: [0]
        }
    ).get_strongly_connected_components(0)
)

print(
    Graph(
        {
            1: [2],
            2: [3, 4],
            3: [4, 6],
            4: [1, 5],
            5: [6],
            6: [7],
            7: [5]
        }
    ).get_strongly_connected_components(3)
)

print(
    Graph(
        {
            0: [2],
            1: [0],
            2: [1],
            3: [2],
            4: [3, 6],
            5: [4],
            6: [5],
            7: [4, 6]
        }
    ).get_strongly_connected_components(7)
)

print(
    Graph(
        {
            0: [1],
            1: [2, 4],
            2: [3],
            3: [2],
            4: [0]
        }
    ).get_strongly_connected_components(0)
)

print(
    Graph(
        {
            1: [2],
            2: [3, 5, 6],
            3: [4, 7],
            4: [3, 8],
            5: [1, 6],
            6: [7],
            7: [6],
            8: [4, 7]
        }
    ).get_strongly_connected_components(1)
)
