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
            Time complexity is O(VE) and space complexity is O(V + E).
        """

        if source not in graph:
            return
        distances = {i: 1e6 for i in graph}
        distances[source] = 0
        # This will take O(V + E) time and O(E) space.
        edges = Solution._get_edges(graph)
        n = len(graph)

        # This will take O(V * E) time.
        for i in range(n - 1):
            for edge in edges:
                src, dst, wt = edge
                if distances[src] + wt < distances[dst]:
                    distances[dst] = distances[src] + wt
        for edge in edges:
            src, dst, wt = edge
            if distances[src] + wt < distances[dst]:
                return -1
        return distances.values()


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
