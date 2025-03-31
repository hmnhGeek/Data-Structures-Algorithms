# Video link - https://www.youtube.com/watch?v=aBxjDBC4M1U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=46


from typing import List


class DisjointSetByRank:
    def __init__(self, nodes: List[int]):
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
            self.parents[ulp_node1] = ulp_node2
            self.ranks[ulp_node2] += 1

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class DisjointSetBySize:
    def __init__(self, nodes: List[int]):
        self.sizes = {i: 1 for i in nodes}
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
        if self.sizes[ulp_node1] <= self.sizes[ulp_node2]:
            self.parents[ulp_node1] = self.parents[ulp_node2]
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = self.parents[ulp_node1]
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


# Example of using disjoint set by rank
dsr = DisjointSetByRank([i for i in range(8)])
dsr.union(1, 2)
dsr.union(2, 3)
dsr.union(4, 5)
dsr.union(6, 7)
dsr.union(5, 6)
# check if 3 and 7 belong to the same component or not
print(dsr.in_same_components(3, 7)) # should return False
dsr.union(3, 7)
print(dsr.in_same_components(3, 7)) # should return True now.


# Example of using disjoint set by size
dss = DisjointSetBySize([i for i in range(8)])
dss.union(1, 2)
dss.union(2, 3)
dss.union(4, 5)
dss.union(6, 7)
dss.union(5, 6)
# check if 3 and 7 belong to the same component or not
print(dss.in_same_components(3, 7)) # should return False
dss.union(3, 7)
print(dss.in_same_components(3, 7)) # should return True now.

