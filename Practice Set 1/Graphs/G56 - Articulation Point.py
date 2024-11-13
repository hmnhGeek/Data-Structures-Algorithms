# Problem link - https://www.naukri.com/code360/library/articulation-points-in-a-graph#:~:text=An%20articulation%20point%20in%20a,also%20known%20as%20cut%20vertices.
# Solution - https://www.youtube.com/watch?v=64KK9K4RpKE


class Graph:
    _tin = 0

    @staticmethod
    def _dfs(graph, node, discovery_time, visited, lowest_time, parents, articulation_points):
        # mark the node as visited.
        visited[node] = True
        # set the discovery time and lowest time of the node as tin.
        discovery_time[node] = lowest_time[node] = Graph._tin
        # increment the timer.
        Graph._tin += 1
        # for this node, set the count of children to 0.
        children = 0
        # iterate on the adjacent nodes of this node.
        for adj_node in graph[node]:
            # if the adjacent node is not visited
            if not visited[adj_node]:
                # we have found a child subgraph of this parent node `node`.
                children += 1
                # set the parent of `adj_node` to `node`.
                parents[adj_node] = node
                # apply DFS on this adjacent node now.
                Graph._dfs(graph, adj_node, discovery_time, visited, lowest_time, parents, articulation_points)
                # once the DFS for this child node is completed, and you get back to the current node, update the lowest
                # time of the current node with that of the adjacent node (it must also have got updated in its dfs
                # call).
                lowest_time[node] = min(lowest_time[node], lowest_time[adj_node])
                # now if the current node is a parent node, i.e., its parent is None, and we found out that it has more
                # than one sub-graph, then first of all it's a root node, and it is an articulation point in the graph.
                # Root node is always the special case of articulation point algorithm.
                if parents[node] is None and children > 1:
                    articulation_points[node] = True
                # if the node is not a root node, and if the lowest time it takes to reach the adjacent (child) node is
                # more than the discovery time of the parent (`node`), then basically you can reach the child node via
                # this parent node only. And thus, this parent node is an articulation point.
                if parents[node] is not None and lowest_time[adj_node] >= discovery_time[node]:
                    articulation_points[node] = True
            # if the adjacent node is visited, then it must be an ancestor of node `node` and not a parent of it.
            if parents[node] != adj_node:
                # if the adjacent node is an ancestor, update the lowest time of the `node` by comparing with the
                # discovery time of this ancestor node as this node can be reached from this ancestor node.
                lowest_time[node] = min(lowest_time[node], discovery_time[adj_node])

    @staticmethod
    def get_articulation_points(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        Graph._tin = 0
        discovery_time = {i: None for i in graph}
        visited = {i: False for i in graph}
        lowest_time = {i: None for i in graph}
        parents = {i: None for i in graph}
        articulation_points = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Graph._dfs(graph, node, discovery_time, visited, lowest_time, parents, articulation_points)

        # print all the articulation points
        for node in articulation_points:
            if articulation_points[node]:
                print(node, end=" ")
        print()


# Graph.get_articulation_points(
#     {
#         0: [1, 2, 3],
#         1: [0],
#         2: [0, 3, 4, 5],
#         3: [0, 2],
#         4: [2, 6],
#         5: [2, 6],
#         6: [4, 5]
#     }
# )


Graph.get_articulation_points(
    {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2, 4],
        4: [3, 5],
        5: [4]
    }
)

Graph.get_articulation_points(
    {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D", "E"],
        "D": ["B", "C", "E"],
        "E": ["C", "D", "F", "G"],
        "F": ["E", "G"],
        "G": ["E", "F"]
    }
)