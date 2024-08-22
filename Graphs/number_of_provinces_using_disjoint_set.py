class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union_by_size(self, node1, node2):
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


class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def get_num_components(self):
        disjoint_set = DisjointSet(list(self.graph.keys()))
        connected_components = 0

        for node in self.graph:
            for adj_node in self.graph[node]:
                if not disjoint_set.in_same_component(node, adj_node):
                    disjoint_set.union_by_size(node, adj_node)

        for parent in disjoint_set.parents:
            if parent == disjoint_set.parents[parent]:
                connected_components += 1

        return connected_components


g1 = Graph(
    {
        1: [2],
        2: [1, 3],
        3: [2],
        4: [5],
        5: [4],
        6: [7],
        7: [6]
    }
)
print(g1.get_num_components())

g2 = Graph(
    {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: []
    }
)
print(g2.get_num_components())