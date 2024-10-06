# Problem link - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# Solution - https://www.youtube.com/watch?v=zQ3zgFypzX4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=12


class Graph:
    @staticmethod
    def _dfs_has_cycle(graph, node, parent, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if visited[adj_node] and adj_node != parent:
                return True
            elif not visited[adj_node]:
                if Graph._dfs_has_cycle(graph, adj_node, node, visited):
                    return True
        return False

    @staticmethod
    def has_cycle(graph):
        visited = {i: False for i in graph}
        for node in visited:
            if not visited[node]:
                if Graph._dfs_has_cycle(graph, node, None, visited):
                    return True
        return False


print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [5],
            3: [1, 4, 6],
            4: [3],
            5: [7],
            6: [3, 7],
            7: [5, 6]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            0: [],
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
    )
)

print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [1],
            3: [1, 4],
            4: [3],
            5: [],
            6: [],
            7: [8],
            8: [7]
        }
    )
)

print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [1, 5, 6],
            3: [1, 4, 7],
            4: [3],
            5: [2],
            6: [2],
            7: [3, 8],
            8: [7]
        }
    )
)

print(
    Graph.has_cycle(
        {
            1: [2, 3],
            2: [1, 5],
            3: [1, 4, 7],
            4: [3, 8],
            5: [2],
            6: [],
            7: [3, 8],
            8: [4, 7]
        }
    )
)