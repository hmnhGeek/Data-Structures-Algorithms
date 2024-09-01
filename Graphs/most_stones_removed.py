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
    # If number of stones is N, then the time complexity is O(N^2) and space complexity is O(N^2 + N) for matrix and DS.

    n = len(mtx)
    m = len(mtx[0])

    # get all the 1-cells from the matrix; their coordinates and the node numbers
    stones = get_stones(mtx, n, m)

    # A stone is of type (i, j, node_number); initialize a disjoint set with node numbers
    disjoint_set = DisjointSet([i[2] for i in stones])

    # connect all the nodes based on same rows into a single component
    for stone in stones:
        x, y, node = stone
        for adj_stone in stones:
            x0, y0, adj_node = adj_stone
            if x == x0:
                disjoint_set.union_by_rank(node, adj_node)

    # connect all the nodes based on same columns into a single component
    for stone in stones:
        x, y, node = stone
        for adj_stone in stones:
            x0, y0, adj_node = adj_stone
            if y == y0:
                disjoint_set.union_by_rank(node, adj_node)

    # as per the video solution, the number of stones that can be removed from a component is
    # equal to the number of nodes in that component - 1. If there are x components and each component
    # has x1, x2, x3, x4, ... number of nodes, then (x1 + x2 + x3 + x4 + ... = N), i.e., total number
    # of nodes in the matrix. Now, the number of stones that can be removed from each component is
    # (x1 - 1 + x2 - 1 + x3 - 1 + x4 - 1 + ... = N - 1*number_of_components). That's what is returned at last.
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