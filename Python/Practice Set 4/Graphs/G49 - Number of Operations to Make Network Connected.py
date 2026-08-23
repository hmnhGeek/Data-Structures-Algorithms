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

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)

    def get_num_components(self):
        count = 0
        for node in self.parents:
            if self.parents[node] == node:
                count += 1
        return count


class Solution:
    @staticmethod
    def get_num_ops(edges, n):
        ds = DisjointSet([i for i in range(n)])
        extra_edges_count = 0
        for u, v in edges:
            if ds.in_same_components(u, v):
                extra_edges_count += 1
            ds.union(u, v)
        if extra_edges_count >= ds.get_num_components() - 1:
            return ds.get_num_components() - 1
        return -1


print(Solution.get_num_ops([[0, 1], [0, 2], [1, 2]], 4))
print(Solution.get_num_ops([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 6))
print(Solution.get_num_ops([[0, 1], [0, 2], [0, 3], [1, 2]], 6))
print(Solution.get_num_ops(
    [
        [1, 2],
        [2, 3],
        [0, 3],
        [0, 1],
        [0, 2],
        [4, 5],
        [5, 6],
        [7, 8]
    ], 9
))
