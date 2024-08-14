# Explanation - https://www.youtube.com/watch?v=aBxjDBC4M1U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=46

class DisjointSet:
    '''This code remains the same as in disjoint_set.py file. Read comments there.'''
    def __init__(self, size):
        self.size = [1]*(size + 1)
        self.parent = [i for i in range(size + 1)]

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        ult_par_u = self.find_ultimate_parent(u)
        ult_par_v = self.find_ultimate_parent(v)

        if ult_par_u == ult_par_v:
            return

        if self.size[ult_par_u] < self.size[ult_par_v]:
            self.parent[ult_par_u] = ult_par_v
        else:
            self.parent[ult_par_v] = ult_par_u
            if self.size[ult_par_v] == self.size[ult_par_u]:
                # The only difference between rank and size approach is that the rank increments by 1 unit
                # only whereas the size increments by the amount of size of smaller sized subtree.
                self.size[ult_par_v] += self.size[ult_par_u]

    def in_same_set(self, u, v):
        return self.find_ultimate_parent(u) == self.find_ultimate_parent(v)


# Example usage of DisjointSet.
ds = DisjointSet(7)
ds.union_by_size(1, 2)
ds.union_by_size(2, 3)
ds.union_by_size(4, 5)
ds.union_by_size(6, 7)
ds.union_by_size(5, 6)
print(ds.in_same_set(3, 7))
ds.union_by_size(3, 7)
print(ds.in_same_set(3, 7))