class Graph:
    @staticmethod
    def _dfs(graph, node, visited, path_visited, safe_nodes):
        visited[node] = True
        path_visited[node] = True
        all_adjacent_nodes_safe = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                all_adjacent_nodes_safe = all_adjacent_nodes_safe and Graph._dfs(graph, adj_node, visited, path_visited,
                                                                                 safe_nodes)
            elif path_visited[adj_node]:
                all_adjacent_nodes_safe = False
            else:
                all_adjacent_nodes_safe = all_adjacent_nodes_safe and safe_nodes[adj_node]
        safe_nodes[node] = all_adjacent_nodes_safe
        path_visited[node] = False
        return all_adjacent_nodes_safe

    @staticmethod
    def safe_nodes(graph):
        visited = {i: False for i in graph}
        path_visited = {i: False for i in graph}
        safe_nodes = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                ans = Graph._dfs(graph, node, visited, path_visited, safe_nodes)
        return safe_nodes


print(
    Graph.safe_nodes(
        {
            1: [2],
            2: [3],
            3: [4, 5],
            4: [6],
            5: [6],
            6: [7],
            7: [],
            8: [1, 9],
            9: [10],
            10: [8],
            11: [9]
        }
    )
)
