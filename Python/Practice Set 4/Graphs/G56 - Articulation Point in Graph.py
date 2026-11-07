# Problem link - https://www.naukri.com/code360/library/articulation-points-in-a-graph#:~:text=An%20articulation%20point%20in%20a,also%20known%20as%20cut%20vertices.
# Solution - https://www.youtube.com/watch?v=64KK9K4RpKE


class Solution:
    @staticmethod
    def get_articulation_points(graph):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """
        visited = {i: False for i in graph}
        low = {i: 1 for i in graph}
        tin = {i: 1 for i in graph}
        art_pts = {i: False for i in graph}
        timer = [0]
        for node in graph:
            if not visited[node]:
                Solution._dfs(node, None, visited, low, tin, art_pts, timer, graph)
        result = []
        for node in art_pts:
            if art_pts[node]:
                result.append(node)
        print(result)

    @staticmethod
    def _dfs(node, parent, visited, low, tin, art_pts, timer, graph):
        visited[node] = True
        low[node] = tin[node] = timer[0]
        timer[0] += 1
        children = 0
        for adj_node in graph[node]:
            if adj_node == parent:
                continue
            elif not visited[adj_node]:
                Solution._dfs(adj_node, node, visited, low, tin, art_pts, timer, graph)
                low[node] = min(low[node], low[adj_node])
                if low[adj_node] >= tin[node] and parent is not None:
                    art_pts[node] = True
                children += 1
            else:
                low[node] = min(low[node], tin[adj_node])
        if children > 1 and parent is None:
            art_pts[node] = True


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
