# Explanation - https://www.youtube.com/watch?v=YbY8cVwWAvw

class FloydWarshall:
    '''
        Floyd-Warshall Algorithm, unlike Dijkstra and Bellman-Ford, is used to calculate
        the shortest paths from each node to every other node. Therefore, we need to use
        a matrix representation to display all those distances.

        The time complexity is O(V^3) and space complexity is O(V^2).
    '''
    def __init__(self, adj_list):
        self.graph = adj_list

    def _build_adj_mtx(self):
        # This method builds the adjacency matrix from the adjacency list in O(V^2) time.
        # It also consumes O(V^2) space.

        n = len(self.graph)
        # create a blank adjacency matrix, with initial distances as infinite for every node.
        mtx = [[float('inf') for _ in range(n)] for _ in range(n)]

        # loop on the adjacency matrix
        for i in range(n):
            for j in range(n):
                # to get from node i to node i, the distance incurred should be 0 and not infinite.
                if i == j:
                    mtx[i][j] = 0
                else:
                    # in the source node i, find the adjacent node j and update the weight in adjacency
                    # matrix.
                    for adj in self.graph[i]:
                        adj_node, edge_wt = adj
                        if adj_node == j:
                            mtx[i][j] = edge_wt

        # return the created adjacency matrix.
        return mtx

    def get_shortest_paths(self):
        # get the adjacency matrix in O(V^2) time.
        adj_mtx = self._build_adj_mtx()

        # the whole idea of Floyd-Warshall is that there is a "via" node through
        # which we will compute the distances from nodes i to j. Let that via node be
        # `k`. If you get a better distance from i to j, via k, adj_mtx[i][j] with that
        # distance, else keep it as is.
        for k in range(len(self.graph)):
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    adj_mtx[i][j] = min(adj_mtx[i][j], adj_mtx[i][k] + adj_mtx[k][j])

        # finally, check the diagonal. If any node has a negative weight, then it means
        # there is a negative cycle in the graph because from node i to itself, the weight
        # should always be 0, and it can become negative only if there is a negative cycle.
        # It can't become > 0 for positive cycle, because this algorithm only updates for
        # minimum distances and in positive cycle, the weights will continuously increase.
        for i in range(len(self.graph)):
            if adj_mtx[i][i] < 0:
                return -1

        # finally return the adjacency matrix with the shortest path from each node to every
        # other node.
        return adj_mtx


sp1 = FloydWarshall(
    {
        0: [[1, 5]],
        1: [[2, -2], [5, -3]],
        2: [[4, 3]],
        3: [[2, 6], [4, -2]],
        4: [],
        5: [[3, 1]]
    }
).get_shortest_paths()

for row in sp1:
    print(row)

print()

sp2 = FloydWarshall(
    {
        0: [[3, 6]],
        1: [[0, 4], [2, 6]],
        2: [],
        3: [[1, 2]]
    }
).get_shortest_paths()

for row in sp2:
    print(row)

print()

sp3 = FloydWarshall(
    {
        0: [],
        1: [[0, 4], [2, -6]],
        2: [[3, 5]],
        3: [[1, -2]]
    }
).get_shortest_paths()

print(sp3)