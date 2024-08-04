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


def dfs(graph, node, visited, path_visited, stack):
    # mark the node as visited and path visited.
    visited[node] = True
    path_visited[node] = True

    # for adjacent node in graph's node
    for adj_node in graph[node]:
        # if the node is not visited, run a dfs on it.
        if not visited[adj_node]:
            # at any point, if a cycle is detected, return True and no need for adding this node into the stack.
            if dfs(graph, adj_node, visited, path_visited, stack):
                return True

        # if the node is visited and path visited also, there's a cycle, return True, no need to add on stack.
        if path_visited[adj_node]:
            return True

    # if there are no nodes, or the adjacent nodes are not getting into a cycle, push the node to the stack.
    stack.push(node)

    # unmark the pushed node, because it's a safe node and we don't want it to give false negative (that there's a
    # cycle) where there is another path leading to the same safe node. Return false, no cycle is there.
    path_visited[node] = False
    return False


def get_safe_nodes(graph):
    # This function uses topological sort with time complexity O(V + E) and space complexity is O(V).

    # initialize a visited and path visited dictionary to track traversal and detect loops (if any).
    visited = {i: False for i in graph}
    path_visited = {i: False for i in graph}

    # stack will be used to store safe nodes.
    stack = Stack()

    # to run on all the connected components.
    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited, path_visited, stack)

    while not stack.is_empty():
        print(stack.pop(), end=" ")


get_safe_nodes(
    {
        1: [2],
        2: [3],
        3: [4, 7],
        4: [5],
        5: [6],
        6: [],
        7: [5],
        8: [2, 9],
        9: [10],
        10: [8]
    }
)

print()
get_safe_nodes(
    {
        0: [1, 2],
        1: [2, 3],
        2: [5],
        3: [0],
        4: [5],
        5: [],
        6: []
    }
)

print()
get_safe_nodes(
    {
        0: [1],
        1: [2],
        2: [0, 3],
        3: []
    }
)