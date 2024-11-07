# Problem link - https://www.geeksforgeeks.org/problems/number-of-provinces/1
# Solution - https://www.youtube.com/watch?v=ZGr5nX-Gi6Y&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=48


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
            self.sizes[ulp_node1] = self.sizes[ulp_node2]

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)

    def get_num_components(self):
        count = 0
        for parent in self.parents:
            if parent == self.parents[parent]:
                count += 1
        return count


class Solution:
    @staticmethod
    def get_provinces(graph):
        """
            Overall time complexity is O(n^2) and space complexity is O(n).
        """

        # Takes O(n) space.
        ds = DisjointSet([i for i in range(len(graph))])

        # Takes O(n^2) time.
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i != j and graph[i][j] == 1 and not ds.in_same_components(i, j):
                    ds.union(i, j)

        # returns count in O(n) time.
        return ds.get_num_components()


print(
    Solution.get_provinces(
        [
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 1]
        ]
    )
)

print(
    Solution.get_provinces(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(
    Solution.get_provinces(
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)
