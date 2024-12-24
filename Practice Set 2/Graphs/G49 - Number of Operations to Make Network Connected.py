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
    def num_ops(edges, n):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        # in O(V) space, create a disjoint set
        ds = DisjointSet([i for i in range(n)])

        # store a variable to count extra edges
        extra_edges = 0

        # loop on the edges of the graph in O(E) time.
        for edge in edges:
            u, v = edge
            # if u and v are not in the same component, connect them.
            if not ds.in_same_component(u, v):
                ds.union(u, v)
            else:
                # else this is an extra edge in this component
                extra_edges += 1

        # now get the number of components in O(V) time.
        nc = ds.num_components()

        # if the number of edges required to connect these components <= extra edges, then we can perform the
        # connections in nc - 1 min operations.
        if nc - 1 <= extra_edges:
            return nc - 1

        # else it is not possible, return -1.
        return -1


print(Solution.num_ops([[0, 1], [0, 2], [1, 2]], 4))
print(Solution.num_ops([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 6))
print(Solution.num_ops([[0, 1], [0, 2], [0, 3], [1, 2]], 6))
