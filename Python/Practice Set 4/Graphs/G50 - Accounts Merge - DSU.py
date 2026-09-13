class DisjointSet:
    def __init__(self, nodes):
        self.parents = {i: i for i in nodes}
        self.sizes = {i: 1 for i in nodes}

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
        if self.sizes[node1] <= self.sizes[node2]:
            self.parents[node1] = node2
            self.sizes[node2] += self.sizes[node1]
        else:
            self.parents[node2] = node1
            self.sizes[node1] += self.sizes[node2]

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)
