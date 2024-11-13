# Problem link - https://www.geeksforgeeks.org/bridge-in-a-graph/
# Solution - https://www.youtube.com/watch?v=qrAub5z8FeA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=55


class Graph:
    _tin = 1

    @staticmethod
    def _dfs(graph, visited, t_low, tin, parent, node, bridges):
        # mark the node as visited, and make low and insertion time both as Graph._tin.
        visited[node] = True
        tin[node] = Graph._tin
        t_low[node] = Graph._tin

        # increment the global timer.
        Graph._tin += 1

        # run DFS on the adjacent nodes of the current node.
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Graph._dfs(graph, visited, t_low, tin, node, adj_node, bridges)

            # once you are back from one of the adjacent node, before moving to the next
            # adjacent node, check if the adjacent node is not parent and if not, update
            # the low time of the current node.
            if adj_node != parent:
                t_low[node] = min(t_low[node], t_low[adj_node])

        # once all the adjacent nodes are visited, and you're about to back-track to the parent,
        # check if the low time of parent is less than that of current node or not. If it is, then
        # (parent, node) is a bridge.
        if parent is not None:
            if t_low[parent] < t_low[node]:
                bridges.append((parent, node))

    @staticmethod
    def find_bridges(graph):
        # ensure that you reset time of insertion to 1 before starting up with the algorithm.
        Graph._tin = 1

        # create a list to store the bridges.
        bridges = []

        # for each node, define time of insertion, lowest time of insertion and visited array.
        t_low = {i: 0 for i in graph}
        tin = {i: 0 for i in graph}
        visited = {i: False for i in graph}

        # typical DFS.
        for node in graph:
            if not visited[node]:
                Graph._dfs(graph, visited, t_low, tin, None, node, bridges)

        # return the bridges.
        return bridges


print(
    Graph.find_bridges(
        {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1],
            3: [1]
        }
    )
)

print(
    Graph.find_bridges(
        {
            1: [2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 5],
            5: [4, 6],
            6: [5, 7, 9],
            7: [6, 8],
            8: [7, 9, 10],
            9: [6, 8],
            10: [8, 11, 12],
            11: [10, 12],
            12: [10, 11]
        }
    )
)

print(
    Graph.find_bridges(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1],
            3: [0, 4],
            4: [3]
        }
    )
)

print(
    Graph.find_bridges(
        {
            0: [1, 2],
            1: [0, 2, 3, 4, 6],
            2: [0, 1],
            3: [1, 5],
            4: [1, 5],
            5: [3, 4],
            6: [1]
        }
    )
)

print(
    Graph.find_bridges(
        {
            0: [1],
            1: [2],
            2: [3],
            3: [4],
            4: []
        }
    )
)