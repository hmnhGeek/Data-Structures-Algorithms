class DisjointSet:
    def __init__(self, nodes):
        self.parents = {i: i for i in nodes}
        self.ranks = {i: 0 for i in nodes}

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
        if self.ranks[ulp_node1] < self.ranks[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
        elif self.ranks[ulp_node1] > self.ranks[ulp_node2]:
            self.parents[ulp_node2] = ulp_node1
        else:
            self.parents[ulp_node1] = ulp_node2
            self.ranks[ulp_node2] += 1

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Solution:
    @staticmethod
    def num_islands_2(n, m, cells):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        nodes = [(m * cell[0]) + cell[1] for cell in cells]
        disjoint_set = DisjointSet(nodes)
        result = []
        for cell in cells:
            x, y = cell
            node = x*m + y
            visited[x][y] = 1
            neighbours = Solution._get_neighbours(x, y, n, m, visited)
            for neighbour in neighbours:
                i, j = neighbour
                adj_node = i*m + j
                disjoint_set.union(node, adj_node)
            result.append(Solution._get_num_components(visited, disjoint_set, m))
        return result

    @staticmethod
    def _get_neighbours(i, j, n, m, visited):
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
    def _get_num_components(visited, ds, m):
        count = 0
        for node in ds.parents:
            if ds.parents[node] == node and visited[node // m][node % m] == 1:
                count += 1
        return count


print(Solution.num_islands_2(4, 5, [(1, 1), (0, 1), (3, 3), (3, 4)]))
print(Solution.num_islands_2(4, 5, [(0, 0), (1, 1), (2, 2), (3, 3)]))
print(Solution.num_islands_2(3, 3, [(0, 1), (0, 1), (1, 2), (2, 1)]))
print(Solution.num_islands_2(2, 2, [(0, 0), (1, 1)]))
print(Solution.num_islands_2(1, 1, [(0, 0)]))
print(Solution.num_islands_2(4, 5, [
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
]))
