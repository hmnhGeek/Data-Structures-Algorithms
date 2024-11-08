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
        if self.sizes[ulp_node1] <= self.sizes[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = ulp_node1
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class MakeLargeIsland:
    def __init__(self, mtx):
        self.mtx = mtx

    def get_neighbours(self, i, j, n, m):
        result = []

        if 0 <= i - 1 < n and self.mtx[i - 1][j] == 1:
            result.append((i - 1, j))
        if 0 <= j + 1 < m and self.mtx[i][j + 1] == 1:
            result.append((i, j + 1))
        if 0 <= i + 1 < n and self.mtx[i + 1][j] == 1:
            result.append((i + 1, j))
        if 0 <= j - 1 < m and self.mtx[i][j - 1] == 1:
            result.append((i, j - 1))

        return result

    def make(self):
        n, m = len(self.mtx), len(self.mtx[0])
        ds = DisjointSet([i for i in range(n*m)])
        largest = 1

        for i in range(n):
            for j in range(m):
                if self.mtx[i][j] == 1:
                    neighbours = self.get_neighbours(i, j, n, m)
                    node = i*m + j
                    for neighbour in neighbours:
                        x, y = neighbour
                        adj_node = x*m + y
                        if not ds.in_same_components(node, adj_node):
                            ds.union(node, adj_node)

        for i in range(n):
            for j in range(m):
                if self.mtx[i][j] == 0:
                    neighbours = self.get_neighbours(i, j, n, m)
                    hash_set = set()
                    node = i*m + j
                    for neighbour in neighbours:
                        x, y = neighbour
                        adj_node = x*m + y
                        hash_set.add(ds.find_ultimate_parent(adj_node))
                    island_size = 0
                    for temp_node in hash_set:
                        island_size += ds.sizes[temp_node]
                    island_size += 1
                    largest = max(largest, island_size)
        return largest


print(
    MakeLargeIsland(
        [
            [1, 1],
            [0, 1]
        ]
    ).make()
)

print(
    MakeLargeIsland(
        [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
        ]
    ).make()
)