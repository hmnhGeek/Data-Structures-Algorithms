# Problem link - https://www.geeksforgeeks.org/problems/number-of-islands/1
# Solution - https://www.youtube.com/watch?v=Rn6B-Q4SNyA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=51


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
        # mark the cell in visited matrix as True.
        self.visited[i][j] = True

        # get the neighbouring cells for the cell (i, j) in O(1) time and space.
        neighbouring_cells = self.get_neighbours(i, j)

        # get the node number from the (i, j). This will be used in the disjoint set as disjoint set only understands
        # integer values.
        node = i*self.m + j

        # assume that addition of this cell into the landmass contribute to a new island altogether.
        self.num_islands += 1

        # loop on the neighbouring cells; this loop will run at max 4 times for 4 neighbours and disjoint set ops are
        # also constant time. Hence, the overall time complexity is O(1). Space used is for visited matrix, which would
        # be O(m*n).
        for neighbour in neighbouring_cells:
            x, y = neighbour

            # fetch the node number for the adjacent node; to be used in disjoint set
            adj_node = x*self.m + y

            # if the adjacent node is visited, then basically the `node` and `adjacent node` can merge into a single
            # connected component, i.e., island
            if self.visited[x][y]:
                # so, if they are already not in a same component, group them into one. Also, decrement the contribution
                # made by cell (i, j) into num_islands because now this cell does not have an individual existence.
                if not self.disjoint_set.in_same_component(node, adj_node):
                    self.disjoint_set.union_by_rank(node, adj_node)
                    self.num_islands -= 1

    def live_track(self, cells):
        # Overall time complexity is O(k + m*n) = O(m*n). The factor m*n is coming because we have to construct the
        # visited array, and also we need to give space for it which makes the space complexity as O(m*n).

        # This function gives the number of islands at each instance of addition of a new cell as an island.
        track = []
        # iterate over each cell in the cells array and if the cell is not previously visited, mark it as a land. This
        # will run depending upon the length of cells array. Assume it to be `k`.
        for i, j in cells:
            if not self.visited[i][j]:
                # This takes O(1) time.
                self.mark_land(i, j)
            # at each instance, append the number of islands into a list which we will return.
            track.append(self.num_islands)
        # return the number of islands at each instance.
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