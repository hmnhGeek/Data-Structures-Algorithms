class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        ulp_node1 = self.find_ultimate_parent(node1)
        ulp_node2 = self.find_ultimate_parent(node2)

        if ulp_node1 == ulp_node2:
            return

        if self.sizes[ulp_node1] < self.sizes[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = ulp_node1
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)

    def get_num_components(self, visited, m):
        count = 0
        for i in self.parents:
            if self.parents[i] == i and visited[i // m][i % m] == 1:
                count += 1
        return count


class Solution:
    @staticmethod
    def _get_valid_neighbours(visited, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and visited[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and visited[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and visited[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and visited[i][j - 1] == 1:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def num_islands_2(n, m, arr):
        num_nodes = n * m
        visited = [[0 for _ in range(m)] for _ in range(n)]
        ds = DisjointSet([i for i in range(num_nodes)])
        result = []
        for cell in arr:
            i, j = cell
            node = i * m + j
            if visited[i][j] == 0:
                visited[i][j] = 1
                neighbours = Solution._get_valid_neighbours(visited, i, j, n, m)
                for neighbour in neighbours:
                    x, y = neighbour
                    adj_node = x * m + y
                    if not ds.in_same_component(node, adj_node):
                        ds.union(node, adj_node)
            result.append(ds.get_num_components(visited, m))
        return result


print(Solution.num_islands_2(4, 5, [(1, 1), (0, 1), (3, 3), (3, 4)]))
print(Solution.num_islands_2(4, 5, [(0, 0), (1, 1), (2, 2), (3, 3)]))
print(Solution.num_islands_2(3, 3, [(0, 1), (0, 1), (1, 2), (2, 1)]))
print(Solution.num_islands_2(2, 2, [(0, 0), (1, 1)]))
print(Solution.num_islands_2(1, 1, [(0, 0)]))
print(Solution.num_islands_2(
    4, 5,
    [
        (0, 0),
        (0, 0),
        (1, 1),
        (1, 0),
        (0, 1),
        (0, 3),
        (1, 3),
        (0, 4),
        (3, 2),
        (2, 2),
        (1, 2),
        (0, 2)
    ]
))
