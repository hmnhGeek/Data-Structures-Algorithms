class DisjointSet:
    def __init__(self, size):
        self.rank = [0]*(size + 1)
        self.parent = [i for i in range(size + 1)]

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ult_pr_u = self.find_ultimate_parent(u)
        ult_pr_v = self.find_ultimate_parent(v)

        if ult_pr_u == ult_pr_v:
            return
        if self.rank[ult_pr_u] < self.rank[ult_pr_v]:
            # attach the smaller rank node's ultimate parent with bigger rank node's ultimate parent
            self.parent[ult_pr_u] = ult_pr_v
        else:
            # attach the smaller rank node's ultimate parent with bigger rank node's ultimate parent
            self.parent[ult_pr_v] = ult_pr_u

            # if however, the rank of both the nodes is same, then the rank of that node will INCREASE
            # BY 1 which has become the ultimate parent of the smaller ranked ultimate parent.
            if self.rank[ult_pr_u] == self.rank[ult_pr_v]:
                self.rank[ult_pr_u] += 1

ds = DisjointSet(7)
ds.union_by_rank(1, 2)
ds.union_by_rank(2, 3)
ds.union_by_rank(4, 5)
ds.union_by_rank(6, 7)
ds.union_by_rank(5, 6)

if ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7):
    print("Same")
else:
    print("Not same")

ds.union_by_rank(3, 7)

if ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7):
    print("Same")
else:
    print("Not same")
