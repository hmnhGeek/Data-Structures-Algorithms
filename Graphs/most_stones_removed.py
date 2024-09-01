class DisjointSet:
    def __init__(self, nodes):
        self.ranks = {i: 0 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union_by_rank(self, node1, node2):
        ulp_node1 = self.find_ultimate_parent(node1)
        ulp_node2 = self.find_ultimate_parent(node2)

        if ulp_node1 == ulp_node2:
            return

        if self.ranks[ulp_node1] < self.ranks[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
        elif self.ranks[ulp_node2] < self.ranks[ulp_node1]:
            self.parents[ulp_node2] = ulp_node1
        else:
            self.parents[ulp_node2] = ulp_node1
            self.ranks[ulp_node1] += 1

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)

    def get_num_components(self):
        count = 0
        for node in self.parents:
            if node == self.parents[node]:
                count += 1
        return count


def get_stones(mtx, n, m):
    stones = set()
    for i in range(n):
        for j in range(m):
            if mtx[i][j] == 1:
                stones.add((i, j, i*m + j))
    return stones


def remove_stones(mtx):
    n = len(mtx)
    m = len(mtx[0])
    stones = get_stones(mtx, n, m)
    disjoint_set = DisjointSet([i[2] for i in stones])

    for stone in stones:
        x, y, node = stone
        for adj_stone in stones:
            x0, y0, adj_node = adj_stone
            if x == x0:
                disjoint_set.union_by_rank(node, adj_node)

    for stone in stones:
        x, y, node = stone
        for adj_stone in stones:
            x0, y0, adj_node = adj_stone
            if y == y0:
                disjoint_set.union_by_rank(node, adj_node)

    return len(stones) - disjoint_set.get_num_components()


print(
    remove_stones(
        [
            [1, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
)

print(
    remove_stones(
        [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0]
        ]
    )
)