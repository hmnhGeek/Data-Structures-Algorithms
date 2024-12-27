class Solution:
    _timer = 1

    @staticmethod
    def _find_bridges(graph, node, parent, visited, in_time, min_time, bridges):
        visited[node] = True
        in_time[node] = min_time[node] = Solution._timer
        Solution._timer += 1
        for adj_node in graph[node]:
            if adj_node == parent:
                continue
            elif not visited[adj_node]:
                Solution._find_bridges(graph, adj_node, node, visited, in_time, min_time, bridges)
                min_time[node] = min(min_time[node], min_time[adj_node])
                if min_time[adj_node] > in_time[node]:
                    bridges.append((node, adj_node))
            else:
                min_time[node] = min(min_time[node], min_time[adj_node])

    @staticmethod
    def get_bridges(graph, source):
        if source not in graph:
            return
        visited = {i: False for i in graph}
        in_time = {i: 0 for i in graph}
        min_time = {i: 0 for i in graph}
        bridges = []
        Solution._find_bridges(graph, source, None, visited, in_time, min_time, bridges)
        return bridges


print(
    Solution.get_bridges(
        {
            1: [2, 4],
            2: [1, 3],
            3: [2, 4],
            4: [1, 3, 5],
            5: [4, 6],
            6: [5, 7, 9],
            7: [6, 8],
            8: [7, 9, 10],
            9: [6, 8],
            10: [8, 11],
            11: [10, 12],
            12: [10, 11]
        },
        1
    )
)

print(
    Solution.get_bridges(
        {
            0: [1, 2],
            1: [0, 2, 3],
            2: [1, 0],
            3: [1]
        },
        0
    )
)

print(
    Solution.get_bridges(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [1, 0],
            3: [0, 4],
            4: [3]
        },
        2
    )
)

print(
    Solution.get_bridges(
        {
            0: [1, 2],
            1: [0, 2, 6, 4, 3],
            2: [0, 1],
            3: [1, 5],
            4: [1, 5],
            5: [3, 4],
            6: [1]
        },
        3
    )
)

print(
    Solution.get_bridges(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        },
        1
    )
)
