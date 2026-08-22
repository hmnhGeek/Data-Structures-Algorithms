# Problem link - https://www.naukri.com/code360/problems/find-the-number-of-states_1377943
# Solution - https://www.youtube.com/watch?v=ZGr5nX-Gi6Y&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=48


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
    def get_number_of_provinces(mtx):
        """
            Time complexity is O(V^2) and space complexity is O(V).
        """
        n = len(mtx)
        ds = DisjointSet([i for i in range(n)])
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if mtx[i][j] == 1:
                    ds.union(i, j)
        return ds.get_num_components()
    

print(
    Solution.get_number_of_provinces(
        [
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0]
        ]
    )
)

print(
    Solution.get_number_of_provinces(
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    )
)

print(
    Solution.get_number_of_provinces(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(Solution.get_number_of_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(Solution.get_number_of_provinces(
    [[1, 1, 1, 0],
     [1, 1, 1, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 1]]
))
