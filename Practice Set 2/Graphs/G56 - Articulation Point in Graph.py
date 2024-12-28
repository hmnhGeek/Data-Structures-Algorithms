# Problem link - https://www.naukri.com/code360/library/articulation-points-in-a-graph#:~:text=An%20articulation%20point%20in%20a,also%20known%20as%20cut%20vertices.
# Solution - https://www.youtube.com/watch?v=64KK9K4RpKE


class Solution:
    _timer = 0

    @staticmethod
    def _dfs(graph, node, parent, tin, low, visited, state):
        visited[node] = True
        tin[node] = low[node] = Solution._timer
        Solution._timer += 1
        child = 0
        for adj_node in graph[node]:
            if adj_node == parent:
                continue
            elif not visited[adj_node]:
                Solution._dfs(graph, adj_node, node, tin, low, visited, state)
                low[node] = min(low[node], low[adj_node])
                if low[adj_node] >= tin[node] and parent is not None:
                    state[node] = True
                child += 1
            else:
                # it's not a parent and still it is visited, thus, it's an ancestor and it might get removed and
                # therefore, take its insertion time only.
                low[node] = min(low[node], tin[adj_node])
        if child > 1 and parent is None:
            state[node] = True

    @staticmethod
    def get_articulation_points(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        Solution._timer = 0
        tin = {i: 0 for i in graph}
        low = {i: 0 for i in graph}
        visited = {i: False for i in graph}
        articulation_state = {i: False for i in graph}
        for node in graph:
            if not visited[node]:
                Solution._dfs(graph, node, None, tin, low, visited, articulation_state)
        articulation_state = {k: v for k, v in articulation_state.items() if v == True}
        print(list(articulation_state.keys()))


Solution.get_articulation_points(
    {
        0: [1, 2, 3],
        1: [0],
        2: [0, 3, 4, 5],
        3: [0, 2],
        4: [2, 6],
        5: [2, 6],
        6: [4, 5]
    }
)


Solution.get_articulation_points(
    {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2, 4],
        4: [3, 5],
        5: [4]
    }
)

Solution.get_articulation_points(
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

Solution.get_articulation_points(
    {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: []
    }
)