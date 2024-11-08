# Problem link - https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1
# Solution - https://www.youtube.com/watch?v=OwMNX8SPavM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=53


class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parents(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find_ultimate_parents(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        ulp_node1 = self.find_ultimate_parents(node1)
        ulp_node2 = self.find_ultimate_parents(node2)
        if ulp_node1 == ulp_node2:
            return
        if self.sizes[ulp_node1] <= self.sizes[ulp_node2]:
            self.parents[ulp_node1] = self.parents[ulp_node2]
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = self.parents[ulp_node1]
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parents(node1) == self.find_ultimate_parents(node2)


class Solution:
    @staticmethod
    def max_stone_removal(mtx):
        n, m = len(mtx), len(mtx[0])
        ds = DisjointSet([i for i in range(n*m)])

        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    node = i*m + j
                    for j0 in range(m):
                        if j0 != j and mtx[i][j0] == 1:
                            adj_node = i*m + j0
                            if not ds.in_same_components(node, adj_node):
                                ds.union(node, adj_node)
                    for i0 in range(n):
                        if i0 != i and mtx[i0][j] == 1:
                            adj_node = i0*m + j
                            if not ds.in_same_components(node, adj_node):
                                ds.union(node, adj_node)

        num_removed = 0
        for parent in ds.parents:
            if parent == ds.parents[parent]:
                num_removed += (ds.sizes[parent] - 1)
        return num_removed


print(
    Solution.max_stone_removal(
        [
            [1, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1]
        ]
    )
)


print(
    Solution.max_stone_removal(
        [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0]
        ]
    )
)