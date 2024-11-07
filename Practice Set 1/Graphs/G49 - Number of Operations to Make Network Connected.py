# Problem link - https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
# Solution - https://www.youtube.com/watch?v=FYrl7iz9_ZU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=49


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
            self.parents[ulp_node2] = ulp_node1
            self.ranks[ulp_node1] += 1

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)

    def get_num_components(self):
        count = 0
        for parent in self.parents:
            if self.parents[parent] == parent:
                count += 1
        return count


class Solution:
    @staticmethod
    def num_ops(edges, num_vertices):
        """
            Time complexity is O(V + E) and space complexity is O(V).
        """

        ds = DisjointSet([i for i in range(num_vertices)])
        extra_edges = 0
        for edge in edges:
            src, dest = edge
            if not ds.in_same_components(src, dest):
                ds.union(src, dest)
            else:
                extra_edges += 1

        # will take O(V) time.
        required_edges_to_connect_components = ds.get_num_components() - 1
        if extra_edges >= required_edges_to_connect_components:
            return required_edges_to_connect_components
        return -1


print(
    Solution.num_ops(
        [[0, 1], [0, 2], [1, 2]],
        4
    )
)

print(
    Solution.num_ops(
        [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 6
    )
)

print(
    Solution.num_ops(
        [[0, 1], [0, 2], [0, 3], [1, 2]], 6
    )
)
