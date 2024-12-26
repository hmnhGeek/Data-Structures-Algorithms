# Problem link - https://www.geeksforgeeks.org/problems/maximum-connected-group/1
# Solution - https://www.youtube.com/watch?v=lgiz0Oup6gM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=52


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


class Solution:
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

    @staticmethod
    def _connect_components(mtx, ds: DisjointSet, n, m):
        """
            Time complexity is O(4nm) to connect all the 1-cells.
        """
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    node = i * m + j
                    neighbours = Solution._get_neighbours(mtx, i, j, n, m)
                    for neighbour in neighbours:
                        x, y = neighbour
                        adj_node = x * m + y
                        if not ds.in_same_component(node, adj_node):
                            ds.union(node, adj_node)

    @staticmethod
    def _get_largest_island(mtx, ds: DisjointSet, largest_size, n, m):
        """
            Time complexity is O(4nm).
        """

        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 0:
                    ultimate_parents = set()
                    node = i * m + j
                    neighbours = Solution._get_neighbours(mtx, i, j, n, m)
                    for neighbour in neighbours:
                        x, y = neighbour
                        adj_node = x * m + y
                        # store the ultimate parents only in a set to avoid duplicate additions of sizes.
                        ultimate_parents.add(ds.find_ultimate_parent(adj_node))
                    new_island_size = 0
                    for ulp in ultimate_parents:
                        new_island_size += ds.sizes[ulp]
                    # add 1 for 0-cell.
                    new_island_size += 1
                    largest_size[0] = max(largest_size[0], new_island_size)

    @staticmethod
    def make_large_island(mtx):
        # get the dimensions of the matrix.
        n, m = len(mtx), len(mtx[0])
        # create a disjoint set of nm nodes. Thus space consumed will be O(nm).
        ds = DisjointSet([i for i in range(n*m)])
        # connect all the 1-element cells into components. This will take O(4nm) time.
        Solution._connect_components(mtx, ds, n, m)
        # store the largest island out of all the components from the disjoint set. This will take another O(nm) time.
        largest_island_size = [max(ds.sizes.values())]
        # find the largest island by converting each 0 to 1 at a time. This will take another O(4nm) time.
        Solution._get_largest_island(mtx, ds, largest_island_size, n, m)
        return largest_island_size[0]


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
