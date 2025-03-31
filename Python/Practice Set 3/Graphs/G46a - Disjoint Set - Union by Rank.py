# Video - https://www.youtube.com/watch?v=aBxjDBC4M1U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=46


class DisjointSet:
    def __init__(self, nodes):
        self.parents = {i: i for i in nodes}
        self.ranks = {i: 0 for i in nodes}

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
            self.parents[ulp_node1] = ulp_node2
            self.ranks[ulp_node2] += 1

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


dsr = DisjointSet([i for i in range(1, 8)])
dsr.union(1, 2)
dsr.union(2, 3)
dsr.union(4, 5)
dsr.union(6, 7)
dsr.union(5, 6)
print(dsr.in_same_component(3, 7))
dsr.union(3, 7)
print(dsr.in_same_component(3, 7))
