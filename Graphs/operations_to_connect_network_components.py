class DisjointSet:
    def __init__(self, nodes):
        self.ranks = {i: 0 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union_by_rank(self, node1, node2):
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

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def _get_edges(self):
        edge_list = []
        for node in self.graph:
            for adj_node in self.graph[node]:
                edge_list.append([node, adj_node])
        return edge_list

    def _get_connected_components(self, disjoint_set: DisjointSet) -> int:
        num_components = 0
        for node in disjoint_set.parents:
            if disjoint_set.parents[node] == node:
                num_components += 1
        return num_components

    def get_num_operations_to_connect_network(self):
        disjoint_set = DisjointSet(list(self.graph.keys()))
        edge_list = self._get_edges()
        num_extra_edges = 0

        for edge in edge_list:
            source, destination = edge
            if not disjoint_set.in_same_component(source, destination):
                disjoint_set.union_by_rank(source, destination)
            else:
                num_extra_edges += 1

        num_components = self._get_connected_components(disjoint_set)
        least_edges_required_to_form_connection = num_components - 1

        if num_extra_edges >= least_edges_required_to_form_connection:
            return least_edges_required_to_form_connection
        return -1


print(
    Graph(
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1],
            3: []
        }
    ).get_num_operations_to_connect_network()
)

print(
    Graph(
        {
            0: [1, 2, 3],
            1: [0, 2, 3],
            2: [0, 1],
            3: [0, 1],
            4: [],
            5: []
        }
    ).get_num_operations_to_connect_network()
)

print(
    Graph(
        {
            0: [1, 2, 3],
            1: [0, 2],
            2: [0, 1],
            3: [0]
        }
    ).get_num_operations_to_connect_network()
)