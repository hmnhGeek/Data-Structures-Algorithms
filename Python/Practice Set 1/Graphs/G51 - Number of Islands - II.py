# Problem link - https://www.geeksforgeeks.org/problems/number-of-islands/1
# Solution - https://www.youtube.com/watch?v=Rn6B-Q4SNyA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=52


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
    def _get_node(cell: tuple, m):
        x, y = cell
        return m * x + y, x, y

    @staticmethod
    def _visit_and_unify(visited, x, y, node, ds, m, n, count: int):
        if visited[x][y] == 1:
            return count

        visited[x][y] = 1
        count += 1

        if 0 <= x - 1 < n and visited[x - 1][y]:
            adj_node, _, _ = Solution._get_node((x - 1, y), m)
            if not ds.in_same_components(node, adj_node):
                ds.union(node, adj_node)
                count -= 1

        if 0 <= y + 1 < m and visited[x][y + 1]:
            adj_node, _, _ = Solution._get_node((x, y + 1), m)
            if not ds.in_same_components(node, adj_node):
                ds.union(node, adj_node)
                count -= 1

        if 0 <= x + 1 < n and visited[x + 1][y]:
            adj_node, _, _ = Solution._get_node((x + 1, y), m)
            if not ds.in_same_components(node, adj_node):
                ds.union(node, adj_node)
                count -= 1

        if 0 <= y - 1 < m and visited[x][y - 1]:
            adj_node, _, _ = Solution._get_node((x, y - 1), m)
            if not ds.in_same_components(node, adj_node):
                ds.union(node, adj_node)
                count -= 1

        return count

    @staticmethod
    def number_of_islands(n, m, cells):
        ds = DisjointSet([i for i in range(n * m)])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        result = []
        islands = 0
        for cell in cells:
            node, x, y = Solution._get_node(cell, m)
            islands = Solution._visit_and_unify(visited, x, y, node, ds, m, n, islands)
            result.append(islands)
        return result


print(Solution.number_of_islands(4, 5, [(1, 1), (0, 1), (3, 3), (3, 4)]))
print(Solution.number_of_islands(4, 5, [(0, 0), (1, 1), (2, 2), (3, 3)]))
print(Solution.number_of_islands(4, 5, [(0, 0), (0, 0), (1, 1), (1, 0), (0, 1), (0, 3), (1, 3), (0, 4), (3, 2), (2, 2), (1, 2), (0, 2)]))
