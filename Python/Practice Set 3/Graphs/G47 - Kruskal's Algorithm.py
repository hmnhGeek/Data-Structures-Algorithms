# Problem link - https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
# Solution - https://www.youtube.com/watch?v=DMnDM_sxVig&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=47


class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parents[node]:
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


class Solution:
    @staticmethod
    def _get_edges(graph):
        edges = []
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                edges.append((wt, node, adj_node))
        return edges

    @staticmethod
    def get_mst(graph):
        """
            Time complexity is O(V + 2E + E*log(E)) and space complexity is O(V + E).
        """

        # get the edges of the graph in O(V + E) time and O(E) space.
        edges = Solution._get_edges(graph)

        # sort the edges in O(E * log(E)) time.
        edges.sort(key=lambda x: x[0])

        # create a disjoint set of O(V) space.
        disjoint_set = DisjointSet([i for i in graph])

        # create MST variables.
        mst = []
        mst_wt = 0

        # loop in the edges of the graph in O(E) time.
        for edge in edges:
            wt, node1, node2 = edge

            # if the nodes are already connected, do nothing.
            if disjoint_set.in_same_component(node1, node2):
                continue

            # else, append them in mst
            mst.append((node1, node2))
            mst_wt += wt

            # and then union them in O(1) time.
            disjoint_set.union(node1, node2)
        return mst, mst_wt


print(
    Solution.get_mst(
        {
            1: [[2, 2], [4, 1], [5, 4]],
            2: [[1, 2], [3, 3], [4, 3], [6, 7]],
            3: [[2, 3], [4, 5], [6, 8]],
            4: [[5, 9], [1, 1], [2, 3], [3, 5]],
            5: [[1, 4], [4, 9]],
            6: [[2, 7], [3, 8]]
        }
    )
)

print(
    Solution.get_mst(
        {
            0: [[1, 5], [2, 1]],
            1: [[0, 5], [2, 3]],
            2: [[0, 1], [1, 3]]
        }
    )
)
