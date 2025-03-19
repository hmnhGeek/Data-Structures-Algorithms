class DisjointSet:
    def __init__(self, nodes):
        self.ranks = {i: 0 for i in nodes}
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
        if self.ranks[ulp_node1] < self.ranks[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
        elif self.ranks[ulp_node2] < self.ranks[ulp_node1]:
            self.parents[ulp_node2] = ulp_node1
        else:
            self.parents[ulp_node1] = ulp_node2
            self.ranks[ulp_node2] += 1

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)

    def num_components(self):
        count = 0
        for i in self.parents:
            if self.parents[i] == i:
                count += 1
        return count


class Solution:
    @staticmethod
    def num_ops(edges, n):
        # create a disjoint sets with the given nodes in O(n) space.
        disjoint_set = DisjointSet([i for i in range(n)])

        # store the count of extra edges.
        extra_edges = 0

        # loop in the edges list and start joining the nodes in the disjoint set in O(E) time.
        for edge in edges:
            # if the connecting nodes are already in same component, just increase the extra edge count.
            if disjoint_set.in_same_component(edge[0], edge[1]):
                extra_edges += 1
                continue
            # else union them
            disjoint_set.union(edge[0], edge[1])

        # minimum number of edges required to connect the components is num_components - 1.
        num_components = disjoint_set.num_components()

        # if we have enough extra edges, then return this minimum amount.
        if extra_edges >= num_components - 1:
            return num_components - 1

        # else return -1.
        return -1


print(Solution.num_ops([[0, 1], [0, 2], [1, 2]], 4))
print(Solution.num_ops([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 6))
print(Solution.num_ops([[0, 1], [0, 2], [0, 3], [1, 2]], 6))
