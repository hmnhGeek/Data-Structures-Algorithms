class DisjointSet:
    def __init__(self, nodes):
        self.sizes = {i: 1 for i in nodes}
        self.parents = {i: i for i in nodes}

    def find_ultimate_parent(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find_ultimate_parent(self.parents[node])
        return self.parents[node]

    def union_by_size(self, node1, node2):
        ulp_node1 = self.find_ultimate_parent(node1)
        ulp_node2 = self.find_ultimate_parent(node2)

        if ulp_node1 == ulp_node2:
            return

        if self.sizes[ulp_node1] < self.sizes[ulp_node2]:
            self.parents[ulp_node1] = ulp_node2
            self.sizes[ulp_node2] += self.sizes[ulp_node1]
        else:
            self.parents[ulp_node2] = ulp_node1
            self.sizes[ulp_node1] += self.sizes[ulp_node2]

    def in_same_components(self, node1, node2):
        return self.find_ultimate_parent(node1) == self.find_ultimate_parent(node2)


def account_merge(accounts):
    node_map = {}
    for i in range(len(accounts)):
        node_map[i] = accounts[i][0]

    disjoint_set = DisjointSet(list(node_map.keys()))
    temp_set = dict()

    for row in range(len(accounts)):
        for col in range(1, len(accounts[row])):
            email = accounts[row][col]
            if email not in temp_set:
                temp_set[email] = row
            elif temp_set[email] != row:
                disjoint_set.union_by_size(temp_set[email], row)

    result = [[node_map[i]] for i in disjoint_set.parents]
    for node in temp_set:
        parent = temp_set[node]
        ultimate_parent = disjoint_set.find_ultimate_parent(parent)
        result[ultimate_parent].append(node)

    for row in result:
        row[1:] = sorted(row[1:])

    final_result = []
    for row in result:
        if len(row) > 1:
            final_result.append(row)

    return final_result


print(
    account_merge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
         ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"],
         ["John", "johnnybravo@mail.com"]]
    )
)

print(
    account_merge(
        [["Gabe", "Gabe00@m.co", "Gabe3@m.co", "Gabe1@m.co"],
         ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
         ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
    )
)
