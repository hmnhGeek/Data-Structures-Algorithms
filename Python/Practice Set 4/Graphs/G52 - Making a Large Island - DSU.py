class DisjointSet:
    def __init__(self, nodes):
        self.size = {i: 1 for i in nodes}
        self.parent = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        ulp_node1 = self.find_ultimate_parent(node1)
        ulp_node2 = self.find_ultimate_parent(node2)

        if ulp_node1 == ulp_node2:
            return

        if self.size[ulp_node1] < self.size[ulp_node2]:
            self.parent[ulp_node1] = ulp_node2
            self.size[ulp_node2] += self.size[ulp_node1]
        else:
            self.parent[ulp_node2] = ulp_node1
            self.size[ulp_node1] += self.size[ulp_node2]

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Solution:
    @staticmethod
    def make_large_island(mtx):
        n, m = len(mtx), len(mtx[0])
        nodes = Solution._get_nodes_from_island(mtx, n, m)
        disjoint_set = DisjointSet(nodes)
        Solution._form_islands(mtx, disjoint_set, n, m)
        largest_size = max(disjoint_set.size.values())
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 0:
                    ulp_set = set()
                    node = (i * m) + j
                    neighbours = Solution._get_neighbours(mtx, i, j, n, m)
                    for x, y in neighbours:
                        adj_node = (x * m) + y
                        ulp = disjoint_set.find_ultimate_parent(adj_node)
                        ulp_set.add(ulp)
                    total_size = 0
                    for ulp in ulp_set:
                        total_size += disjoint_set.size[ulp]
                    total_size += 1
                    largest_size = max(largest_size, total_size)
        return largest_size

    @staticmethod
    def _get_nodes_from_island(mtx, n, m):
        nodes = []
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    nodes.append((i * m) + j)
        return nodes

    @staticmethod
    def _form_islands(mtx, disjoint_set, n, m):
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    node = (i * m) + j
                    neighbours = Solution._get_neighbours(mtx, i, j, n, m)
                    for x, y in neighbours:
                        adj_node = (x * m) + y
                        disjoint_set.union(node, adj_node)

    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1:
            neighbours.append((i, j - 1))
        return neighbours


print(
    Solution.make_large_island(
        [
            [1, 1],
            [0, 1]
        ]
    )
)

print(
    Solution.make_large_island(
        [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]
    )
)

print(
    Solution.make_large_island(
        [
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1]
        ]
    )
)

print(
    Solution.make_large_island(
        [
            [1, 0, 1, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0]
        ]
    )
)

print(
    Solution.make_large_island(
        [
            [1, 1],
            [1, 1]
        ]
    )
)
