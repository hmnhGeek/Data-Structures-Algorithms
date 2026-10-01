class DisjointSet:
    def __init__(self, nodes):
        self.size = {i: 1 for i in nodes}
        self.parent = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
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
