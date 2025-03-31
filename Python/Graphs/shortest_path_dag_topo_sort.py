class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def is_empty(self):
        return self.length == 0

    def pop(self):
        if self.is_empty():
            return

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        return self.head.data if not self.is_empty() else None

    def _show(self):
        curr = self.head

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


def get_topological_order(graph, node, visited, stack):
    '''Time: O(V + E) and Space: O(E) - Standard DFS time complexity'''

    # as per dfs rule, mark this node as visited
    visited[node] = True

    # for all the adjacent nodes, if they are not visited,
    # apply dfs algorithm on them to find topological order.
    for adj in graph[node]:
        adj_node, wt = adj
        if not visited[adj_node]:
            get_topological_order(graph, adj_node, visited, stack)

    # at the end, ensure that you store the node in the stack.
    stack.push(node)


def get_distance_from_source_node(g):
    '''
        Overall time complexity is O(V + E)
        Overall space complexity is O(V) (for stack) + O(E) for topo sort
    '''

    # initialize an empty stack to store the topological order.
    stack = Stack()
    visited = {i: False for i in g}

    # DFS algo - Time complexity is O(V + E) and space complexity is O(E)
    for node in g:
        if not visited[node]:
            # update the stack by using topological sort function
            get_topological_order(g, node, visited, stack)

    # once the stack is populated with topological order, initialize
    # a `distances` array with distances to each node marked as infinity
    # from the source node (which is the first node in the topological order).
    # also, explicitly mark distance of top node (first node in topological order)
    # as 0 in the distances array.
    distances = {i: float('inf') for i in g}
    distances[stack.top()] = 0

    # while the stack is not empty. This will run V times because stack will have V nodes
    # Time complexity would be O(V + E) (E because inside there is a for loop which runs in
    # total for E times). Also, it is V + E and not V*E because for each vertex V, the loop
    # runs for subset of edges for that vertex only. This is countable, please dry run.
    while not stack.is_empty():
        # extract the nodes in topological order
        node = stack.pop()

        # store the distance taken from source node to the current
        # popped node from the distances array
        parent_distance = distances[node]

        # now loop in all the adjacent nodes of the popped node
        # and update the distances of adjacent nodes by taking the
        # minimum of existing distance and the distance from
        # source node to this node, which would be (parent_distance + wt)
        for adj in g[node]:
            adj_node, wt = adj
            distances[adj_node] = min(distances[adj_node], parent_distance + wt)

    # return the distances once they are updated.
    return distances


print(
    get_distance_from_source_node(
        {
            0: [[1, 2]],
            1: [[3, 1]],
            2: [[3, 3]],
            3: [],
            4: [[0, 3], [2, 1]],
            5: [[4, 1]],
            6: [[4, 2], [5, 3]]
        }
    )
)

print(
    get_distance_from_source_node(
        {
            0: [[1, 2], [4, 1]],
            1: [[2, 3]],
            2: [[3, 6]],
            3: [],
            4: [[2, 2], [5, 4]],
            5: [[3, 1]]
        }
    )
)
