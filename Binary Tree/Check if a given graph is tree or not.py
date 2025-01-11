class Solution:
    @staticmethod
    def _dfs(graph, node, parent, visited):
        visited[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node]:
                if Solution._dfs(graph, adj_node, node, visited):
                    return True
            elif adj_node != parent:
                return True
        return False

    @staticmethod
    def _graph_has_cycle(graph, disconnected):
        visited = {i: False for i in graph}
        num_components = 0
        for node in graph:
            if not visited[node]:
                num_components += 1
                if num_components > 1:
                    disconnected[0] = True
                if Solution._dfs(graph, node, None, visited):
                    return True
        return False

    @staticmethod
    def check_if_tree(graph):
        is_disconnected = [False]
        has_cycle = Solution._graph_has_cycle(graph, is_disconnected)
        if not has_cycle and not is_disconnected[0]:
            return True
        return False


print(
    Solution.check_if_tree(
        {
            0: [1, 2, 3],
            1: [0],
            2: [0],
            3: [0, 4],
            4: [3]
        }
    )
)

print(
    Solution.check_if_tree(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1],
            3: [0, 4],
            4: [3]
        }
    )
)
