# Problem link - https://www.geeksforgeeks.org/problems/number-of-provinces/1
# Solution - https://www.youtube.com/watch?v=ACzkVtewUYA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=7


class Graph:
    @classmethod
    def _dfs(cls, graph, node, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                Graph._dfs(graph, adj_node, visited)

    @staticmethod
    def get_num_components(adjacency_list):
        """
            Overall time complexity is O(V + E) and overall space complexity is O(V).
        """

        # create a visited array for each node which will take O(V) space.
        visited = {i: False for i in adjacency_list}
        # create a num_components variable which will store the number of components in the graph
        num_components = 0
        # loop on each node, this will run for V times. But overall DFS call for V nodes is made.
        for node in visited:
            # if the node is not visited, there is a component to do traversal on.
            if not visited[node]:
                # increase the count of num_components and perform DFS using this node as starting node.
                num_components += 1
                # This will take O(V + E) time and O(V) space.
                Graph._dfs(adjacency_list, node, visited)
        # return the number of components found.
        return num_components


class Solution:
    @staticmethod
    def find_num_provinces(graph):
        # Number of provinces would be equal to the number of components in the graph.
        return Graph.get_num_components(graph)


print(
    Solution.find_num_provinces(
        {
            1: [3],
            2: [],
            3: [1]
        }
    )
)

print(
    Solution.find_num_provinces(
        {
            1: [],
            2: [],
            3: []
        }
    )
)

print(
    Solution.find_num_provinces(
        {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2],
            4: []
        }
    )
)

print(
    Solution.find_num_provinces(
        {
            0: [],
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
    )
)