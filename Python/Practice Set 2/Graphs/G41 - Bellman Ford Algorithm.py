# Problem link - https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
# Solution - https://www.youtube.com/watch?v=0vVofAhAYjc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=41


class Solution:
    @staticmethod
    def _get_edges(graph):
        edges = []
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                edges.append([node, adj_node, wt])
        return edges

    @staticmethod
    def get_shortest_distances(graph, source):
        """
            Time complexity is O(VE) and space is O(V + E).
        """

        # edge case check
        if source not in graph:
            return

        # define distances and set source distance as 0.
        distances = {i: 1e6 for i in graph}
        distances[source] = 0

        # get the edges from the graph in O(V + E) time and O(E) space.
        v = len(graph)
        edges = Solution._get_edges(graph)

        # loop for V - 1 times.
        for i in range(v - 1):
            # Loop on all the edges and relax them if required, in E times iteration.
            for edge in edges:
                u, v, w = edge
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # loop on all the edges in O(E) time.
        for edge in edges:
            u, v, w = edge
            # if any relaxation happens, then it means there is a negative cycle.
            if distances[u] + w < distances[v]:
                return "Negative Cycle Detected!"

        # else, return the shortest paths.
        return list(distances.values())


print(
    Solution.get_shortest_distances(
        {
            0: [[1, 9]],
            1: []
        },
        0
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 5]],
            1: [[0, 3], [2, -1]],
            2: [[0, 1]]
        },
        2
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 5]],
            1: [[2, 1], [3, 2]],
            2: [[4, 1]],
            3: [],
            4: [[3, -1]]
        },
        0
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 4]],
            1: [[2, -6]],
            2: [[3, 5]],
            3: [[1, -2]]
        },
        0
    )
)

print(
    Solution.get_shortest_distances(
        {
            0: [[1, 5]],
            1: [[2, -2], [5, -3]],
            2: [[4, 3]],
            3: [[2, 6], [4, -2]],
            4: [],
            5: [[3, 1]]
        },
        0
    )
)