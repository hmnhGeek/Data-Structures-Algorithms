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
    """
        Overall time complexity is O(n^2) and overall space complexity is O(n^2).
    """

    n = len(mtx)

    # create a disjoint set storing n^2 nodes starting from 0. This will take up O(n^2) space.
    disjoint_set = DisjointSet([i for i in range(n**2)])

    # store max_size that can be obtained by switching one 0 to 1 as -inf.
    max_size = float('-inf')

    # Using O(n^2) time, connect all the connected 1s.
    for i in range(n):
        for j in range(n):
            # if the current cell is a 1, then only there is a point of grouping.
            if mtx[i][j] == 1:
                # to get any node value in disjoint set by the cell coordinates, the formula is node = i*num_cols + j.
                node = i*n + j
                # loop on the 4 neighbours of the current node, and if the neighbour is a 1, then only do a union by
                # size on the disjoint set.
                neighbours = get_neighbours(i, j, n)
                for adj_cell in neighbours:
                    x, y = adj_cell
                    adj_node = x*n + y
                    if mtx[x][y] == 1:
                        disjoint_set.union_by_size(node, adj_node)

    # create a blank set which will be used to store the ultimate parents of each connected component. We are not
    # directly summing up the size of connected components in the below loop (and instead using a set), because it is
    # possible that two or more neighbours of the 0-cell can be part of the same component, and we do not want to
    # add the size of same component multiple times in that case. This will again take O(n^2) time. Also, the set will
    # hold at max 4 distinct components, and so we can say that the set occupies O(1) space. Also, disjoint set
    # operations done above and below take O(1) time at average.
    temp_set = set()
    for i in range(n):
        for j in range(n):
            # if the current cell is 0, then add all the ultimate parents of connected components who have the adjacent
            # 1s of this 0-cell as their nodes.
            if mtx[i][j] == 0:
                neighbours = get_neighbours(i, j, n)
                for adj_cell in neighbours:
                    x, y = adj_cell
                    adj_node = x*n + y
                    if mtx[x][y] == 1:
                        temp_set.add(disjoint_set.find_ultimate_parent(adj_node))

                # once we have all the unique neighbouring components of this 0-cell, add up the sizes of these
                # components, then add 1 for the size of this 0-cell (because we are assuming that we've converted it
                # to a 1). Finally, update the max_size.
                local_size = 0
                for ulp in temp_set:
                    local_size += disjoint_set.sizes[ulp]
                local_size += 1
                max_size = max(max_size, local_size)

                # ensure that you clear the set for next 0-cell.
                temp_set.clear()

    # Now, there could be an edge case when the entire matrix is originally made of all 1s. In that case, max_size will
    # be -inf and will never be modified. In such case, we must update the max size by looping on the matrix once again.
    # This will again take O(n^2) time.
    for node in range(n**2):
        max_size = max(max_size, disjoint_set.sizes[disjoint_set.find_ultimate_parent(node)])

    # return the maximum size that was obtained.
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