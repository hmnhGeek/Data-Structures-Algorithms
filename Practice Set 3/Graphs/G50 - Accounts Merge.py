class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        ulp_node1 = self.find_ultimate_parent(node1)
        ulp_node2 = self.find_ultimate_parent(node2)

        if ulp_node1 == ulp_node2:
            return

        if self.sizes[ulp_node1] <= self.sizes[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = ulp_node1
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Solution:
    @staticmethod
    def accounts_merge(mtx):
        n = len(mtx)
        email_to_node = {}
        disjoint_set = DisjointSet([i for i in range(n)])
        for i in range(n):
            for j in range(1, len(mtx[i])):
                if mtx[i][j] not in email_to_node:
                    email_to_node[mtx[i][j]] = i
                else:
                    disjoint_set.union(email_to_node[mtx[i][j]], i)
        result = {i: set() for i in range(n)}
        final_result = []
        for i in range(n):
            for j in range(1, len(mtx[i])):
                node = email_to_node[mtx[i][j]]
                ulp = disjoint_set.find_ultimate_parent(node)
                result[ulp].add(mtx[i][j])
        for i in result:
            if len(result[i]) > 0:
                name = mtx[i][0]
                emails = list(result[i])
                emails.sort()
                row = [name] + emails
                final_result.append(row)
        return final_result


print(
    Solution.accounts_merge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
         ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"],
         ["John", "johnnybravo@mail.com"]]
    )
)

print(
    Solution.accounts_merge(
        [["Gabe", "Gabe00@m.co", "Gabe3@m.co", "Gabe1@m.co"],
         ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
         ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
    )
)

print(
    Solution.accounts_merge(
        [["John", "j1@com", "j2@com", "j3@com"],
         ["John", "j4@com"],
         ["Raj", "r1@com", "r2@com"],
         ["John", "j1@com", "j5@com"],
         ["Raj", "r2@com", "r3@com"],
         ["Mary", "m1@com"]]
    )
)

print(
    Solution.accounts_merge(
        [
            ["Rohan", "rohan123@gmail.com", "1279ro@gmail.com"],
            ["Rohit", "rohit101@yahoo.com", "hitman30487@gmail.com"],
            ["Rohan", "1279ro@gmail.com", "niemann01@gmail.com"],
            ["Rohan", "kaushik@outlook.com"],
        ]
    )
)