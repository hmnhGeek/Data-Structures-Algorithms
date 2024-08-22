# Problem link - https://www.geeksforgeeks.org/problems/account-merge/1
# Solution - https://www.youtube.com/watch?v=FMwpt_aQOGw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=50


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
    # let's have each row (as an index) as a node in the disjoint set
    disjoint_set = DisjointSet([i for i in range(len(accounts))])

    # create a blank dictionary to map email IDs to the 0th index of every row in accounts
    temp_set = dict()

    # loop on all the email IDs (basically all rows but from 1st cols and 0th col is for name)
    for row in range(len(accounts)):
        for col in range(1, len(accounts[row])):
            # store the current email ID for now.
            email = accounts[row][col]

            # if this email ID is seen for the first time, assign its value in temp set as the
            # row index from which it is picked up (row index represents the name, but since
            # indices are unique, we are using them instead of actual names which can repeat)
            if email not in temp_set:
                temp_set[email] = row

            # however, if in some other row, we again see a same email ID which is already in
            # the dictionary, then the row numbers from the set of this existing email ID and
            # the current different row index must lie in the same component. Use disjoint set
            # to merge them into a single component.
            elif temp_set[email] != row:
                disjoint_set.union_by_size(temp_set[email], row)

    # finally the disjoint set have all the rows from accounts connected appropriately.
    # create a result 2D array and insert the actual names now in each row.
    result = [[accounts[i][0]] for i in range(len(accounts))]

    # start looping on the emails stored in the temp set
    for email in temp_set:
        # get the parent of this email from temp set
        parent = temp_set[email]
        # find the ultimate parent of this parent also (remember, this is an integer value
        # representing an index)
        ultimate_parent = disjoint_set.find_ultimate_parent(parent)
        # and in the result 2D array, append this email to row containing the name of
        # ultimate parent.
        result[ultimate_parent].append(email)

    # finally sort the email IDs
    for row in result:
        row[1:] = sorted(row[1:])

    # now create a final list in which we will store only those rows from result which
    # have some email IDs
    final_result = []
    for row in result:
        # if there is more than just name in the row, add it to final_result
        if len(row) > 1:
            final_result.append(row)

    # finally return final result
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
