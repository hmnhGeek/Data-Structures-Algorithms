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
