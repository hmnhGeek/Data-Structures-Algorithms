# Problem link - https://leetcode.com/problems/accounts-merge/description/
# Solution - https://www.youtube.com/watch?v=FMwpt_aQOGw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=51


class DisjointSet:
    def __init__(self, nodes):
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
            self.parents[ulp_node1] = ulp_node2
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = ulp_node1
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


class Solution:
    @staticmethod
    def _perform_union_operations(ds: DisjointSet, emails_to_node_mapping, accounts, n):
        for row in range(n):
            for email in range(1, len(accounts[row])):
                if accounts[row][email] not in emails_to_node_mapping:
                    emails_to_node_mapping[accounts[row][email]] = row
                else:
                    ds.union(row, emails_to_node_mapping[accounts[row][email]])

    @staticmethod
    def _group_nodes_and_emails(ds: DisjointSet, node_to_emails_mapping, emails_to_node_mapping):
        for email in emails_to_node_mapping:
            ulp_email = ds.find_ultimate_parent(emails_to_node_mapping[email])
            node_to_emails_mapping[ulp_email].append(email)

    @staticmethod
    def _prepare_final_result(node_to_emails_mapping, final_result, name_node_mapping):
        for node in node_to_emails_mapping:
            if len(node_to_emails_mapping[node]) > 0:
                row_to_add = [name_node_mapping[node], ]
                emails_to_add = node_to_emails_mapping[node]
                emails_to_add.sort()
                row_to_add.extend(emails_to_add)
                final_result.append(row_to_add)

    @staticmethod
    def accounts_merge(accounts):
        n = len(accounts)

        # create name and node mappings where name is the 0th index of each row and node is the index of each row.
        name_node_mapping = {i: accounts[i][0] for i in range(n)}

        # create a disjoint set for each node.
        ds = DisjointSet([i for i in name_node_mapping])

        # now we will be looping on all the emails and assign them their parent nodes. At the same time, if the email
        # was found earlier and is now present in the `emails_to_node_mapping`, we will perform union of the current
        # row `node` and the node from already existing key-value pair.
        emails_to_node_mapping = {}
        Solution._perform_union_operations(ds, emails_to_node_mapping, accounts, n)

        # now we will group the emails based on nodes and the emails will be appended to their ultimate parents from
        # the disjoint set.
        node_to_emails_mapping = {i: [] for i in name_node_mapping}
        Solution._group_nodes_and_emails(ds, node_to_emails_mapping, emails_to_node_mapping)

        # finally, using the node-name mapping created above, we will restore the names and sort the emails for each
        # row. Finally return the result.
        final_result = []
        Solution._prepare_final_result(node_to_emails_mapping, final_result, name_node_mapping)
        return final_result


print(
    Solution.accounts_merge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
    )
)

print(
    Solution.accounts_merge(
        [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
    )
)
