# Problem link - https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
# Solution - https://www.youtube.com/watch?v=DMnDM_sxVig&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=47


class QuickSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        QuickSort._sort(arr, 0, n - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def _get_partition_index(arr, low, high):
        i, j = low, high
        pivot = arr[low]
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j


class Edge:
    def __init__(self, wt, source, destination):
        self.wt = wt
        self.src = source
        self.dst = destination

    def __lt__(self, other):
        return self.wt < other.wt

    def __le__(self, other):
        return self.wt <= other.wt

    def __gt__(self, other):
        return self.wt > other.wt

    def __ge__(self, other):
        return self.wt >= other.wt

    def __eq__(self, other):
        return self.wt == other.wt

    def __ne__(self, other):
        return self.wt != other.wt


class DisjointSet:
    def __init__(self, nodes):
        self.parents = {i: i for i in nodes}
        self.ranks = {i: 0 for i in nodes}

    def find_ultimate_parent(self, node):
        if self.parents[node] == node:
            return self.parents[node]
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


class Solution:
    @staticmethod
    def get_mst(graph):
        """
            Time complexity is O(V + 2E + E*log(E)) and space complexity is O(V + E).
        """
        edges = Solution._get_edges(graph)
        QuickSort.sort(edges)
        ds = DisjointSet([node for node in graph])
        mst, mst_wt = [], 0
        for edge in edges:
            w, s, d = edge.wt, edge.src, edge.dst
            if not ds.in_same_components(s, d):
                ds.union(s, d)
                mst_wt += w
                mst.append((s, d))
        return mst, mst_wt

    @staticmethod
    def _get_edges(graph):
        edges = []
        for node in graph:
            for adj_node, wt in graph[node]:
                edges.append(Edge(wt, node, adj_node))
        return edges


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
