class DisjointSet:
    def __init__(self, nodes):
        self.ranks = {i: 0 for i in nodes}
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

        if self.ranks[ulp_node1] < self.ranks[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
        elif self.ranks[ulp_node2] < self.ranks[ulp_node1]:
            self.parents[ulp_node2] = ulp_node1
        else:
            self.parents[ulp_node1] = ulp_node2
            self.ranks[ulp_node2] += 1

    def in_same_component(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Solution:
    @staticmethod
    def _get_emails_to_name_mapping(mtx, disjoint_set: DisjointSet, n):
        """
            Time complexity is O(nm) and space complexity is O(mn).
        """

        temp = {}
        for i in range(n):
            row = mtx[i]
            # loop on the emails of each row
            for email in row[1::]:
                # if the email is in temp and the name index is not yet unified, do the union.
                if email in temp and not disjoint_set.in_same_component(i, temp[email]):
                    disjoint_set.union(i, temp[email])
                else:
                    # else, if it is a new email, assign its parent in temp.
                    temp[email] = i
        return temp

    @staticmethod
    def _unify_emails(emails_to_name_mapping, disjoint_set: DisjointSet, n):
        """
            Time complexity is O(nm + n*m*log(m)) and space complexity is O(nm).
        """

        result = {i: [] for i in range(n)}

        # iterate on the emails from the given mapping.
        for email in emails_to_name_mapping:
            # extract the parent
            parent = emails_to_name_mapping[email]
            # find the ultimate parent
            ulp = disjoint_set.find_ultimate_parent(parent)
            # store the email in the ultimate parent only.
            result[ulp].append(email)

        # sort each row of the result and return only the rows having emails.
        for i in result:
            result[i].sort()
        return {k: v for k, v in result.items() if len(v) != 0}

    @staticmethod
    def _build_result(mtx, unified_emails, n):
        """
            Time complexity is O(nm) and space complexity is O(nm).
        """
        result = []
        for i in unified_emails:
            result.append([mtx[i][0], ] + unified_emails[i])
        return result

    @staticmethod
    def accounts_merge(mtx):
        """
            Time complexity is O(nm * log(m)) and space complexity is O(nm).
        """

        n = len(mtx)
        # construct a disjoint set of n vertices representing the indices of the rows.
        ds = DisjointSet([i for i in range(n)])
        # for each email, get the corresponding names from the matrix.
        emails_to_name_mapping = Solution._get_emails_to_name_mapping(mtx, ds, n)
        # after iterating on the emails to name mapping, unify them in the disjoint set.
        unified_names_to_emails_mapping = Solution._unify_emails(emails_to_name_mapping, ds, n)
        # construct the result and return it.
        result = Solution._build_result(mtx, unified_names_to_emails_mapping, n)
        return result


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
