# Problem link - https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1
# Solution - https://www.youtube.com/watch?v=OwMNX8SPavM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=54


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
            self.parents[ulp_node1] = self.parents[ulp_node2]
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = self.parents[ulp_node1]
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)

    def get_num_components(self):
        count = 0
        for i in self.parents:
            if self.parents[i] == i:
                count += 1
        return count


class Solution:
    @staticmethod
    def _build_disjoint_set(mtx, row, col, nodes):
        """
            Overall time complexity is O(nm) and space complexity is O(nm) assuming all the cells from matrix go into
            the disjoint set.
        """

        n, m = len(mtx), len(mtx[0])
        for i in range(n):
            for j in range(m):
                # get the node that represents this 1-cell.
                if mtx[i][j] == 1:
                    node = i * m + j
                    # add this node to nodes set.
                    nodes.add(node)

                    # add this node to the row in which it is present.
                    if i in row:
                        row[i].append(node)
                    else:
                        row[i] = [node,]

                    # add this node to the column in which it is present.
                    if j in col:
                        col[j].append(node)
                    else:
                        col[j] = [node,]

        # construct the disjoint set with the nodes collected.
        ds = DisjointSet([i for i in nodes])

        # unify all the nodes which lie in the same row.
        for r in row:
            for index in range(1, len(row[r])):
                ds.union(row[r][0], row[r][index])

        # unify all the nodes which lie in the same column.
        for c in col:
            for index in range(1, len(col[c])):
                ds.union(col[c][0], col[c][index])

        # return the disjoint set and the number of nodes which represent the total number of stones as well.
        return ds, len(nodes)

    @staticmethod
    def remove_stones(mtx):
        """
            Overall time complexity is O(nm) and space complexity is O(nm).
        """

        # these variables will be useful for building the disjoint set.
        row_set = dict()
        col_set = dict()
        nodes = set()

        # build the disjoint set and also get the total number of stones.
        disjoint_set, n = Solution._build_disjoint_set(mtx, row_set, col_set, nodes)

        # return the number of stones that can be removed.
        return n - disjoint_set.get_num_components()


print(
    Solution.remove_stones(
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
    Solution.remove_stones(
        [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0]
        ]
    )
)

print(
    Solution.remove_stones(
        [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
        ]
    )
)

print(
    Solution.remove_stones(
        [
            [1, 1],
            [1, 0]
        ]
    )
)

print(
    Solution.remove_stones(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]
        ]
    )
)
