class DisjointSet:
    def __init__(self, nodes):
        self.ranks = {i: 0 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parents[node]:
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
            self.parents[ulp_node1] = ulp_node2
            self.ranks[ulp_node2] += 1

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class NumberOfIslands:
    def __init__(self, n, m):
        self.graph = [[0 for _ in range(m)] for _ in range(n)]
        self.num_islands = 0
        self.n = n
        self.m = m
        self.visited = [[False for _ in range(self.m)] for _ in range(self.n)]
        self.disjoint_set = DisjointSet([i for i in range(self.n * self.m)])

    def get_neighbours(self, i, j):
        neighbours = []

        if 0 <= i - 1 < self.n:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < self.m:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < self.n:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < self.m:
            neighbours.append((i, j - 1))

        return neighbours

    def mark_land(self, i, j):
        self.graph[i][j] = 1
        self.visited[i][j] = True
        neighbouring_cells = self.get_neighbours(i, j)
        node = i*self.m + j
        self.num_islands += 1

        for neighbour in neighbouring_cells:
            x, y = neighbour
            adj_node = x*self.m + y
            if self.graph[x][y] == 1:
                if not self.disjoint_set.in_same_component(node, adj_node):
                    self.disjoint_set.union_by_rank(node, adj_node)
                    self.num_islands -= 1

    def live_track(self, cell):
        track = []
        for i, j in cell:
            if not self.visited[i][j]:
                self.mark_land(i, j)
            track.append(self.num_islands)
        return track


print(
    NumberOfIslands(4, 5).live_track(
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
    )
)

print(
    NumberOfIslands(4, 5).live_track(
        [
            (1, 1),
            (0, 1),
            (3, 3),
            (3, 4)
        ]
    )
)

print(
    NumberOfIslands(4, 5).live_track(
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3)
        ]
    )
)