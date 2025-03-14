# Problem link - https://www.geeksforgeeks.org/strongly-connected-components/
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
    def _reverse_graph(graph):
        """
            Reverse the graph in O(V + E) time and O(V + E) space.
        """
        reversed_graph = {i: [] for i in graph}
        for node in graph:
            for adj_node in graph[node]:
                reversed_graph[adj_node].append(node)
        return reversed_graph

    @staticmethod
    def _dfs(graph, visited, node, stack):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Solution._dfs(graph, visited, adj_node, stack)
        stack.push(node)

    @staticmethod
    def _get_main_stack(graph):
        """
            Compute the reachability of each node in a stack in O(V + E) time and O(V) space using plain DFS.
        """
        stack = Stack()
        visited = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, visited, node, stack)
        return stack

    @staticmethod
    def _get_strongly_connected_components(reversed_graph, main_stack):
        # store the strongly connected components in `result` array.
        result = []
        # stored visited array for doing a DFS on the reversed graph.
        visited = {i: False for i in reversed_graph}

        # while not all the nodes from reachability stack have been used...
        while not main_stack.is_empty():
            # pop the node
            node = main_stack.pop()
            # if the node is not visited
            if not visited[node]:
                # create a new traversal stack and `scc` list to store the nodes of the SCC, as this is a new
                # component that we are starting with. Use DFS to get these nodes.
                traversal_stack = Stack()
                scc = []
                Solution._dfs(reversed_graph, visited, node, traversal_stack)
                while not traversal_stack.is_empty():
                    scc.append(traversal_stack.pop())

                # finally, add this SCC into result list.
                result.append(scc)

        # return the result list.
        return result

    @staticmethod
    def get_strongly_connected_components(graph):
        """
            Overall time complexity is O(V + E) and space complexity is O(V + E).
        """

        # get the reachability of each node in the graph using simple DFS in O(V + E) time and O(V) space.
        main_stack = Solution._get_main_stack(graph)
        # get the reversed graph in O(V + E) time and space. We reverse the graph in order to perform DFS from last
        # finished node in the above main stack and then compute the SCC.
        reversed_graph = Solution._reverse_graph(graph)
        # finally, find and return the strongly connected components using the reversed graph in O(V + E) time and space
        return Solution._get_strongly_connected_components(reversed_graph, main_stack)


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
