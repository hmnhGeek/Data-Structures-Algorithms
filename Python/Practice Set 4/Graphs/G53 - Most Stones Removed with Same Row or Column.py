class DisjointSet:
    def __init__(self, nodes):
        self.size = {i: 1 for i in nodes}
        self.parent = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        ulp_node1 = self.find_ultimate_parent(node1)
        ulp_node2 = self.find_ultimate_parent(node2)
        if ulp_node1 == ulp_node2:
            return
        if self.size[ulp_node1] < self.size[ulp_node2]:
            self.parent[ulp_node1] = ulp_node2
            self.size[ulp_node2] += self.size[ulp_node1]
        else:
            self.parent[ulp_node2] = ulp_node1
            self.size[ulp_node1] += self.size[ulp_node2]

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Solution:
    @staticmethod
    def remove_stones(arr):
        n, m = Solution._find_dimensions(arr)
        nodes = [i for i in range(n)] + [n + j for j in range(m)]
        disjoint_set = DisjointSet(nodes)
        for i, j in arr:
            disjoint_set.union(i, j + n)
        return len(arr) - Solution._compute_valid_components(disjoint_set)

    @staticmethod
    def _find_dimensions(arr):
        i, j = 0, 0
        for x, y in arr:
            if x > i:
                i = x
            if y > j:
                j = y
        return i + 1, j + 1

    @staticmethod
    def _compute_valid_components(disjoint_set):
        count = 0
        for node in disjoint_set.parent:
            if disjoint_set.parent[node] == node and disjoint_set.size[node] > 1:
                count += 1
        return count


print(Solution.remove_stones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
print(Solution.remove_stones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
print(Solution.remove_stones([[0, 0]]))
print(Solution.remove_stones([[0, 1], [1, 0], [0, 0]]))
print(Solution.remove_stones([[2, 0], [2, 1], [3, 1], [3, 2], [5, 5]]))
