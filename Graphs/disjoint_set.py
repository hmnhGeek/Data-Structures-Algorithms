class DisjointSet:
    def __init__(self, size):
        self.rank = [0]*(size + 1)
        self.parent = [i for i in range(size + 1)]

    def find_ultimate_parent(self, node):
        # This is a recursive function which compresses the edges as well.
        # This method takes O(log(n)) time.

        # if a node is parent to itself, then it is the ultimate parent
        if node == self.parent[node]:
            return node

        # find the ultimate parent of the parent of this node, and at the same time
        # compress the edge so that node's parent now directly points to the ultimate
        # parent.
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        # This also takes O(1) time depending upon the `find_ultimate_parent` method.

        # finding the ultimate parents of u and v nodes in O(1) time (only in compression scenarios,
        # does the function takes O(log(n)) time.
        ult_pr_u = self.find_ultimate_parent(u)
        ult_pr_v = self.find_ultimate_parent(v)

        # if the ultimate parents of both the nodes is same, no need to do any union,
        # because they are already a part of same tree.
        if ult_pr_u == ult_pr_v:
            return

        # if the program counter comes here, it means that nodes u and v are not in the same tree.

        # check if the rank of ultimate parent of u < the rank of the ultimate parent of v
        # since v's ultimate parent has a higher rank, assign u's ultimate parent's parent
        # to ultimate parent of v, else do the opposite (in equal case also). We link the
        # lower rank node to the higher rank node so that the height of the higher rank does
        # not increase further.
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

    def in_same_set(self, u, v):
        return self.find_ultimate_parent(u) == self.find_ultimate_parent(v)


# Example usage of DisjointSet.
ds = DisjointSet(7)
ds.union_by_rank(1, 2)
ds.union_by_rank(2, 3)
ds.union_by_rank(4, 5)
ds.union_by_rank(6, 7)
ds.union_by_rank(5, 6)
print(ds.in_same_set(3, 7))
ds.union_by_rank(3, 7)
print(ds.in_same_set(3, 7))
