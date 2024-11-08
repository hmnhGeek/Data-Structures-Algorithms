# Problem link - https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
# Solution - https://www.youtube.com/watch?v=DMnDM_sxVig&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=47


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


class Graph:
    @staticmethod
    def _get_sorted_edges(graph):
        edges = []
        for node in graph:
            for adj in graph[node]:
                adj_node, wt = adj
                edges.append((wt, node, adj_node))
        edges.sort(key=lambda x:x[0])
        return edges

    @staticmethod
    def get_mst(graph):
        """
            Overall time complexity is O(V + E + Elog(E)) and space is O(V + E).
        """

        # O(V + 2E + E*log(E)) time and O(2E) space.
        edges = Graph._get_sorted_edges(graph)
        # O(V) space.
        disjoint_set = DisjointSet([i for i in graph])
        mst_wt = 0
        mst = []

        # O(2E) time.
        for edge_tuple in edges:
            edge_wt, src, dest = edge_tuple
            # in O(1) time
            if not disjoint_set.in_same_components(src, dest):
                # O(1) time
                disjoint_set.union(src, dest)
                mst_wt += edge_wt
                mst.append((src, dest))
        return mst, mst_wt


print(
    Graph.get_mst(
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
    Graph.get_mst(
        {
            0: [[1, 5], [2, 1]],
            1: [[0, 5], [2, 3]],
            2: [[0, 1], [1, 3]]
        }
    )
)