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

    def num_components(self):
        count = 0
        for i in self.parents:
            if i == self.parents[i]:
                count += 1
        return count


class Solution:
    @staticmethod
    def _get_neighbours(mtx, x, y, n, m):
        neighbours = []
        if 0 <= x - 1 < n and mtx[x - 1][y] == 1:
            neighbours.append((x - 1, y))
        if 0 <= y + 1 < m and mtx[x][y + 1] == 1:
            neighbours.append((x, y + 1))
        if 0 <= x + 1 < n and mtx[x + 1][y] == 1:
            neighbours.append((x + 1, y))
        if 0 <= y - 1 < m and mtx[x][y - 1] == 1:
            neighbours.append((x, y - 1))
        return neighbours

    @staticmethod
    def _connect_islands(mtx, disjoint_set, n, m):
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    node = i * m + j
                    neighbours = Solution._get_neighbours(mtx, i, j, n, m)
                    for neighbour in neighbours:
                        x, y = neighbour
                        adj_node = x * m + y
                        if not disjoint_set.in_same_component(node, adj_node):
                            disjoint_set.union(node, adj_node)

    @staticmethod
    def make_large_island(mtx):
        n, m = len(mtx), len(mtx[0])

        # define a disjoint set of size O(nm)
        disjoint_set = DisjointSet([i for i in range(n * m)])

        # connect all the islands given in problem in O(nm) time.
        Solution._connect_islands(mtx, disjoint_set, n, m)

        # define a hash set to store the ultimate parents of all the adjacent components of a 0-cell.
        hash_set = set()

        # store the size of largest island.
        largest_island_size = max(disjoint_set.sizes.values())

        # loop in the matrix in O(nm) time (it will not be O(nm) in avg case but only in worst case).
        for i in range(n):
            for j in range(m):
                # if a 0-cell is found.
                if mtx[i][j] == 0:
                    # get the neighbouring cells of this 0-cell which are 1.
                    neighbours = Solution._get_neighbours(mtx, i, j, n, m)

                    # loop in the neighbours and add their ultimate parents into the hash set.
                    for neighbour in neighbours:
                        x, y = neighbour
                        adj_node = x * m + y
                        hash_set.add(disjoint_set.find_ultimate_parent(adj_node))

                    # get the island's size which will be formed if this 0-cell is added to the group of islands.
                    island_size = 0
                    for parent in hash_set:
                        island_size += disjoint_set.sizes[parent]
                    island_size += 1

                    # update the largest island size.
                    largest_island_size = max(largest_island_size, island_size)

                    # restore the hash set.
                    hash_set.clear()
        return largest_island_size


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