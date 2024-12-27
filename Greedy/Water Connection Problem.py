class Solution:
    @staticmethod
    def _get_graph(sources, destinations, pipes):
        graph = {i: [] for i in sources}
        for i in destinations:
            if i not in graph:
                graph[i] = []

        out_degree = {i: 0 for i in graph}
        in_degree = {i: 0 for i in graph}

        for i in range(len(sources)):
            graph[sources[i]].append([destinations[i], pipes[i]])
            out_degree[sources[i]] += 1
            in_degree[destinations[i]] += 1
        return graph, out_degree, in_degree

    @staticmethod
    def _dfs(graph, node, visited, min_diameter, final_destination, out_degree):
        if out_degree[node] == 0:
            final_destination.append(node)
        visited[node] = True
        for adj in graph[node]:
            adj_node, wt = adj
            min_diameter[0] = min(min_diameter[0], wt)
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited, min_diameter, final_destination, out_degree)

    @staticmethod
    def make_water_connections(sources, destinations, pipes):
        graph, out_degree, in_degree = Solution._get_graph(sources, destinations, pipes)
        visited = {i: False for i in graph}
        num_components = 0
        for node in graph:
            if not visited[node] and in_degree[node] == 0:
                min_diameter = [1e6]
                final_destination = []
                num_components += 1
                Solution._dfs(graph, node, visited, min_diameter, final_destination, out_degree)
                print(node, final_destination[0], min_diameter[0])
        return num_components


print(Solution.make_water_connections([7, 5, 4, 2, 9, 3], [4, 9, 6, 8, 7, 1], [98, 72, 10, 22, 17, 66]))
