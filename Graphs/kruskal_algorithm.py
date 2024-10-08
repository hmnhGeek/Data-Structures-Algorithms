# Problem link - https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
# Solution - https://www.youtube.com/watch?v=DMnDM_sxVig

class DisjointSet:
    def __init__(self, nodes):
        self.ranks = {i: 0 for i in nodes}
        self.parents = {node: node for node in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union_by_rank(self, node1, node2):
        up_node1 = self.find_ultimate_parent(node1)
        up_node2 = self.find_ultimate_parent(node2)

        if up_node1 == up_node2:
            return

        if self.ranks[up_node1] < self.ranks[up_node2]:
            self.parents[up_node1] = up_node2
            self.ranks[up_node2] += 1
        elif self.ranks[up_node2] < self.ranks[up_node1]:
            self.parents[up_node2] = up_node1
            self.ranks[up_node1] += 1
        else:
            self.parents[up_node2] = up_node1

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class KruskalAlgorithm:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def _get_sorted_edges_list(self):
        # The time complexity would be O(V + E + E*log(E)) and space complexity would be O(E).
        edge_list = []

        for node in self.graph:
            for adj in self.graph[node]:
                adj_node, edge_wt = adj
                edge_list.append([edge_wt, node, adj_node])

        edge_list.sort(key=lambda x: x[0])
        return edge_list

    def get_minimum_spanning_tree(self):
        # Overall time complexity is O(V + E{1 + log(E) + 4*alpha}) and space complexity is O(V + E).

        # Get the sorted edge list in O(V + E + E*log(E)) time and O(E) space.
        edge_list = self._get_sorted_edges_list()

        # Initialize a disjoint set containing nodes from the graph. This will take O(V) space.
        disjoint_set = DisjointSet(list(self.graph.keys()))

        # Initialize variables for MST.
        minimum_spanning_tree = []
        minimum_spanning_tree_wt = 0

        # This loop will run for E times. Hence, time complexity would be O(E*4*alpha). The idea
        # behind this loop is to check if the source and destination nodes are in same component
        # or not. If they are not, connect them with edge_wt. Next time, if we get same source
        # and destination nodes, they will be already connected with a smaller weight, and hence
        # it would be a MST. Ensure to increase the MST weight also.
        for edge in edge_list:
            edge_wt, source, dest = edge
            # union and components check will take O(4*alpha) time
            if not disjoint_set.in_same_components(source, dest):
                disjoint_set.union_by_rank(source, dest)
                minimum_spanning_tree.append(edge)
                minimum_spanning_tree_wt += edge_wt

        # finally return the MST variables.
        return minimum_spanning_tree, minimum_spanning_tree_wt


def example_usage_of_disjoint_set_class():
    ds = DisjointSet([1, 2, 3, 4, 5, 6, 7])
    ds.union_by_rank(1, 2)
    ds.union_by_rank(2, 3)
    ds.union_by_rank(4, 5)
    ds.union_by_rank(6, 7)
    ds.union_by_rank(5, 6)
    print(ds.in_same_components(3, 7))
    print(ds.in_same_components(5, 7))
    ds.union_by_rank(3, 7)
    print(ds.in_same_components(3, 7))


print(
    KruskalAlgorithm(
        {
            1: [[2, 2], [4, 1], [5, 4]],
            2: [[1, 2], [4, 3], [3, 3], [6, 7]],
            3: [[2, 3], [4, 5], [6, 8]],
            4: [[1, 1], [2, 3], [3, 5], [5, 9]],
            5: [[1, 4], [4, 9]],
            6: [[3, 8], [2, 7]]
        }
    ).get_minimum_spanning_tree()
)

print(
    KruskalAlgorithm(
        {
            0: [[1, 4], [7, 8]],
            1: [[0, 4], [2, 8], [7, 11]],
            2: [[1, 8], [3, 7], [8, 2]],
            3: [[2, 7], [4, 9], [5, 14]],
            4: [[3, 9], [5, 10]],
            5: [[2, 4], [3, 14], [4, 10], [6, 2]],
            6: [[5, 2], [7, 1], [8, 6]],
            7: [[0, 8], [1, 11], [6, 1], [8, 7]],
            8: [[2, 2], [6, 6], [7, 7]]
        }
    ).get_minimum_spanning_tree()
)

print(
    KruskalAlgorithm(
        {
            0: [[1, 5], [2, 1]],
            1: [[0, 5], [2, 3]],
            2: [[0, 1], [1, 3]]
        }
    ).get_minimum_spanning_tree()
)