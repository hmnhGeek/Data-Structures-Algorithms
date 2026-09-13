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


class Solution:
    @staticmethod
    def accounts_merge(mtx):
        disjoint_set = DisjointSet([i for i in range(len(mtx))])
        nodes_to_name_mapping = Solution._get_nodes_to_name_mapping(mtx)
        emails_to_node_mapping = Solution._get_emails_to_node_mapping(mtx, disjoint_set)
        merged_nodes_to_emails_mapping = Solution._get_merged_mapping(emails_to_node_mapping, disjoint_set, nodes_to_name_mapping)
        return Solution._merged_result(merged_nodes_to_emails_mapping, nodes_to_name_mapping)

    @staticmethod
    def _get_nodes_to_name_mapping(mtx):
        mapping = {}
        for i in range(len(mtx)):
            mapping[i] = mtx[i][0]
        return mapping

    @staticmethod
    def _get_emails_to_node_mapping(mtx, ds):
        mapping = {}
        for i in range(len(mtx)):
            for j in range(1, len(mtx[i])):
                email = mtx[i][j]
                if email not in mapping:
                    mapping[email] = i
                else:
                    ds.union(i, mapping[email])
        return mapping

    @staticmethod
    def _get_merged_mapping(emails_to_node_mapping, ds, nodes_to_name_mapping):
        merged_mapping = {i: [] for i in nodes_to_name_mapping}
        for email in emails_to_node_mapping:
            ulp = ds.find_ultimate_parent(emails_to_node_mapping[email])
            merged_mapping[ulp].append(email)
        return {i: merged_mapping[i] for i in merged_mapping if len(merged_mapping[i]) > 0}

    @staticmethod
    def _merged_result(merged_nodes_to_emails_mapping, nodes_to_name_mapping):
        result = []
        for node in merged_nodes_to_emails_mapping:
            row = [nodes_to_name_mapping[node], ]
            merged_nodes_to_emails_mapping[node].sort()
            row.extend(merged_nodes_to_emails_mapping[node])
            result.append(row)
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
