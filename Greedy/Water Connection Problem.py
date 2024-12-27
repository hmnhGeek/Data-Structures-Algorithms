class Solution:
    @staticmethod
    def _get_graph(sources, destinations, pipes):
        # create the blank graph by using nodes from sources and destinations.
        graph = {i: [] for i in sources}
        for i in destinations:
            if i not in graph:
                graph[i] = []

        # store in and out degrees of all the nodes in the graph.
        out_degree = {i: 0 for i in graph}
        in_degree = {i: 0 for i in graph}

        # update these variables and return them
        for i in range(len(sources)):
            graph[sources[i]].append([destinations[i], pipes[i]])
            out_degree[sources[i]] += 1
            in_degree[destinations[i]] += 1
        return graph, out_degree, in_degree

    @staticmethod
    def _dfs(graph, node, visited, min_diameter, final_destination, out_degree):
        # if this is the final node from the graph, add it.
        if out_degree[node] == 0:
            final_destination.append(node)
        # mark the node as visited
        visited[node] = True
        for adj in graph[node]:
            adj_node, wt = adj
            # update the min diameter pipe.
            min_diameter[0] = min(min_diameter[0], wt)
            if not visited[adj_node]:
                Solution._dfs(graph, adj_node, visited, min_diameter, final_destination, out_degree)

    @staticmethod
    def make_water_connections(sources, destinations, pipes):
        # get the graph and the in and out degrees of each node.
        graph, out_degree, in_degree = Solution._get_graph(sources, destinations, pipes)

        # blank visited array for DFS
        visited = {i: False for i in graph}

        # get the number of components
        num_components = 0

        # loop on the nodes of the graph
        for node in graph:
            # if the node is not visited, and it's the first node in the component, then start a DFS from it.
            if not visited[node] and in_degree[node] == 0:
                # store the min diameter of this component and the final destination.
                min_diameter = [1e6]
                final_destination = []
                # increase the number of components.
                num_components += 1
                # perform the DFS.
                Solution._dfs(graph, node, visited, min_diameter, final_destination, out_degree)
                # print the tank and tap with min pipe diameter.
                print(node, final_destination[0], min_diameter[0])
        return num_components


print(Solution.make_water_connections([7, 5, 4, 2, 9, 3], [4, 9, 6, 8, 7, 1], [98, 72, 10, 22, 17, 66]))
print(Solution.make_water_connections([1, 3], [2, 4], [60, 50]))
