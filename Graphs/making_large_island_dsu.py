class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union_by_size(self, node1, node2):
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

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


def get_neighbours(i, j, n):
    neighbours = []

    if 0 <= i - 1 < n:
        neighbours.append((i - 1, j))
    if 0 <= j + 1 < n:
        neighbours.append((i, j + 1))
    if 0 <= i + 1 < n:
        neighbours.append((i + 1, j))
    if 0 <= j - 1 < n:
        neighbours.append((i, j - 1))

    return neighbours


def make_large_island(mtx):
    n = len(mtx)
    disjoint_set = DisjointSet([i for i in range(n**2)])
    max_size = float('-inf')

    for i in range(n):
        for j in range(n):
            if mtx[i][j] == 1:
                node = i*n + j
                neighbours = get_neighbours(i, j, n)
                for adj_cell in neighbours:
                    x, y = adj_cell
                    adj_node = x*n + y
                    if mtx[x][y] == 1:
                        disjoint_set.union_by_size(node, adj_node)
    temp_set = set()
    for i in range(n):
        for j in range(n):
            if mtx[i][j] == 0:
                neighbours = get_neighbours(i, j, n)
                for adj_cell in neighbours:
                    x, y = adj_cell
                    adj_node = x*n + y
                    if mtx[x][y] == 1:
                        temp_set.add(disjoint_set.find_ultimate_parent(adj_node))
                local_size = 0
                for ulp in temp_set:
                    local_size += disjoint_set.sizes[ulp]
                local_size += 1
                max_size = max(max_size, local_size)
                temp_set.clear()
    return max_size


print(
    make_large_island(
        [
            [1, 1],
            [0, 1]
        ]
    )
)

print(
    make_large_island(
        [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]
    )
)

print(
    make_large_island(
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
    make_large_island(
        [
            [1, 0],
            [0, 1]
        ]
    )
)