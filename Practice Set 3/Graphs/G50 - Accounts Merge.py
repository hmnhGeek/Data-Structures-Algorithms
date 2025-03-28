# Problem link - https://www.geeksforgeeks.org/problems/account-merge/1
# Solution - https://www.youtube.com/watch?v=FMwpt_aQOGw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=50


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
    def _construct_email_to_node_mapping(disjoint_set, email_to_node, mtx, n):
        for i in range(n):
            for j in range(1, len(mtx[i])):
                if mtx[i][j] not in email_to_node:
                    email_to_node[mtx[i][j]] = i
                else:
                    disjoint_set.union(email_to_node[mtx[i][j]], i)

    @staticmethod
    def _construct_result(disjoint_set, result, email_to_node, mtx, n):
        for i in range(n):
            for j in range(1, len(mtx[i])):
                node = email_to_node[mtx[i][j]]
                ulp = disjoint_set.find_ultimate_parent(node)
                result[ulp].add(mtx[i][j])

    @staticmethod
    def _construct_final_result(final_result, result, mtx):
        for i in result:
            if len(result[i]) > 0:
                name = mtx[i][0]
                emails = list(result[i])
                emails.sort()
                row = [name] + emails
                final_result.append(row)

    @staticmethod
    def accounts_merge(mtx):
        """
            Time complexity is O(nm * log(m)) and space complexity is O(nm).
        """

        n = len(mtx)

        # construct a disjoint set of size O(n).
        disjoint_set = DisjointSet([i for i in range(n)])

        # construct a mapping of email to name node in O(n*m) time and O(n*m) space.
        email_to_node = {}
        Solution._construct_email_to_node_mapping(disjoint_set, email_to_node, mtx, n)

        # construct result set in O(nm) time and O(nm) space.
        result = {i: set() for i in range(n)}
        Solution._construct_result(disjoint_set, result, email_to_node, mtx, n)

        # construct the final DSU result in O(nm) time and O(nm*log(m)) space.
        final_result = []
        Solution._construct_final_result(final_result, result, mtx)
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