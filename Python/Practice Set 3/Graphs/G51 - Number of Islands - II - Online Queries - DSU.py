# Problem link - https://www.geeksforgeeks.org/problems/number-of-islands/1
# Solution - https://www.youtube.com/watch?v=Rn6B-Q4SNyA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=51


class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parents[node]:
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
        elif self.sizes[ulp_node2] < self.sizes[ulp_node1]:
            self.parents[ulp_node2] = ulp_node1
            self.sizes[ulp_node1] += self.sizes[ulp_node2]
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
    def _get_components_count(ds, mtx, n, m):
        count = 0
        for node in ds.parents:
            # increment the count of components only for those nodes which have value 1.
            if node == ds.parents[node] and mtx[node // m][node % m] == 1:
                count += 1
        return count

    @staticmethod
    def num_islands_2(n, m, queries):
        """
            Time complexity is O(nm) and space complexity is O(nm).
        """

        # create a disjoint set of size O(nm)
        ds = DisjointSet([i for i in range(n * m)])

        # define a matrix to mark the islands in size O(nm).
        mtx = [[0 for j in range(m)] for i in range(n)]

        # define a query result.
        result = []

        # loop on the queries.
        for q in queries:
            x, y = q

            # mark this island and get the node representation of this cell.
            mtx[x][y] = 1
            node = x * m + y

            # find the neighbours of this node in O(1) time.
            neighbours = Solution._get_neighbours(mtx, x, y, n, m)
            for neighbour in neighbours:
                x0, y0 = neighbour
                adj_node = x0 * m + y0

                # if the adjacent node is not in same component, union them in constant time.
                if not ds.in_same_component(node, adj_node):
                    ds.union(node, adj_node)

            # append the count of components in the result variable.
            result.append(Solution._get_components_count(ds, mtx, n, m))

        # return the result.
        return result


print(Solution.num_islands_2(4, 5, [(1, 1), (0, 1), (3, 3), (3, 4)]))
print(Solution.num_islands_2(4, 5, [(0, 0), (1, 1), (2, 2), (3, 3)]))
print(Solution.num_islands_2(3, 3, [(0, 1), (0, 1), (1, 2), (2, 1)]))
print(Solution.num_islands_2(2, 2, [(0, 0), (1, 1)]))
print(Solution.num_islands_2(1, 1, [(0, 0)]))
print(Solution.num_islands_2(4, 5, [
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
]))
