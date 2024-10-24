# Problem link - https://www.geeksforgeeks.org/problems/course-schedule/1
# Solution - https://www.youtube.com/watch?v=WAOfKpxYHR8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=24


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


class Graph:
    @staticmethod
    def _dfs(graph, node, visited, path_visited, stack):
        # mark the node as visited and path visited.
        visited[node] = True
        path_visited[node] = True

        # iterate on the adjacent nodes of the graph.
        for adj_node in graph[node]:
            # if the adjacent node is not visited, start a DFS from this adjacent node.
            if not visited[adj_node]:
                has_cycle = Graph._dfs(graph, adj_node, visited, path_visited, stack)
                # if a cycle is detected from this adjacent node, return True. No need
                # to worry about stack now.
                if has_cycle:
                    return True
            # if the node is visited and path visited, there's a cycle, return True.
            elif path_visited[adj_node]:
                return True

        # finally, unmark the node from path visited and push it to stack for topological sorting.
        path_visited[node] = False
        stack.push(node)

        # return False as no cycle is detected.
        return False

    @staticmethod
    def get_topological_sort(edges):
        """
            This is a DFS approach and hence the time complexity is O(V + E) and space
            complexity is O(V).
        """

        # form the adjacency list from the list of edges.
        graph = Graph._from_edge_list(edges)

        # create visited and path visited arrays to detect a cycle.
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}

        # maintain a stack to perform topological sort.
        stack = Stack()

        # iterate on the nodes of the graph
        for node in visited:
            # if the current node is not visited, perform a DFS starting from this node.
            if not visited[node]:
                # if there is a cycle detected, break, no need to perform further topological
                # sort as course schedule is not possible in a cyclic graph.
                if Graph._dfs(graph, node, visited, path_visited, stack):
                    print(-1)
                    return

        # if no cycle was detected, spit out the topological order or the course schedule order
        # from the stack.
        while not stack.is_empty():
            print(stack.pop(), end=" ")
        print()

    @staticmethod
    def _from_edge_list(edges):
        """
            This method constructs the adjacency list from a edge list in O(E) time.
        """
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
        return graph


Graph.get_topological_sort([[0, 1]])
Graph.get_topological_sort([[0, 1], [0, 2], [1, 3], [2, 3]])
Graph.get_topological_sort([[0, 1], [1, 0]])