# Problem link - https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1
# Solution - https://www.youtube.com/watch?v=OwMNX8SPavM&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=54


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
        elif self.ranks[ulp_node1] > self.ranks[ulp_node2]:
            self.parents[ulp_node2] = ulp_node1
        else:
            self.parents[ulp_node1] = ulp_node2
            self.ranks[ulp_node2] += 1

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Solution:
    @staticmethod
    def remove_stones(stones):
        """
            Time complexity is O(m + n) and space complexity is O(m + n).
        """

        # get the max row and max column indices using a for loop in O(n) time.
        max_row, max_col = -1e6, -1e6
        for stone in stones:
            max_row = max(max_row, stone[0])
            max_col = max(max_col, stone[1])

        # create the disjoint set of size O(m), where m denotes `max_row + max_col` order.
        nodes = [i for i in range(max_row + 1)] + [j + max_row + 1 for j in range(max_col + 1)]
        disjoint_set = DisjointSet(nodes)

        # create a set to store the rows and columns (or nodes in terms of disjoint set) which have at least one
        # stone in them. This will take O(n) space only.
        nodes_having_stones = set()

        # now loop on all the stones in O(n) time.
        for stone in stones:
            # get the nodes and union them.
            node1, node2 = stone[0], stone[1] + max_row + 1
            disjoint_set.union(node1, node2)

            # add these nodes into the set also.
            nodes_having_stones.add(node1)
            nodes_having_stones.add(node2)

        # count the number of components using only the nodes which had at least one stone in them.
        num_components = 0
        for node in nodes_having_stones:
            if disjoint_set.parents[node] == node:
                num_components += 1

        # return the max possible stones count that can be removed.
        return len(stones) - num_components


print(Solution.remove_stones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
print(Solution.remove_stones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
print(Solution.remove_stones([[0, 0]]))
print(Solution.remove_stones([[0, 1], [1, 0], [0, 0]]))
print(Solution.remove_stones([[2, 0], [2, 1], [3, 1], [3, 2], [5, 5]]))
