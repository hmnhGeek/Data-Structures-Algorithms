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
        n, m = len(mtx), len(mtx[0])
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    node = i * m + j
                    nodes.add(node)
                    if i in row:
                        row[i].append(node)
                    else:
                        row[i] = [node,]
                    if j in col:
                        col[j].append(node)
                    else:
                        col[j] = [node,]
        ds = DisjointSet([i for i in nodes])
        for r in row:
            for index in range(1, len(row[r])):
                ds.union(row[r][0], row[r][index])
        for c in col:
            for index in range(1, len(col[c])):
                ds.union(col[c][0], col[c][index])
        return ds, len(nodes)

    @staticmethod
    def remove_stones(mtx):
        row_set = dict()
        col_set = dict()
        nodes = set()
        disjoint_set, n = Solution._build_disjoint_set(mtx, row_set, col_set, nodes)
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
