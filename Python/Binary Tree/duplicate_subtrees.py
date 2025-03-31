# Problem link - https://www.geeksforgeeks.org/problems/duplicate-subtrees/1
# Solution - https://www.youtube.com/watch?v=m0dG99f5ct4


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def solve_duplicate_subtrees(root, mp, result):
    # Time complexity is O(N^2) because we are visiting every node again and again for each subtree
    # Space complexity is O(N).

    # This is the base case, if node is None, return "N" denoting a null node.
    if root is None:
        return "N"

    # get the subtree string for root, i.e., root.data, left_subtree_string, right_subtree_string
    subtree_string = f"{root.data},{solve_duplicate_subtrees(root.left, mp, result)},{solve_duplicate_subtrees(root.right, mp, result)}"

    # if the subtree at root's string is in map already
    if subtree_string in mp:
        # check if the subtree has been identified second time only.
        if mp[subtree_string] == 1:
            # if yes, then add it in the result
            result.append(root.data)
        # irrespective, increment the subtree count.
        mp[subtree_string] += 1
    else:
        # if encountered for the first time, make its count 1.
        mp[subtree_string] = 1

    # return the subtree string which will be used by other recursion calls
    return subtree_string


def find_duplicate_subtrees(root):
    mp = {}
    result = []
    solve_duplicate_subtrees(root, mp, result)
    # print all those subtrees whose count is more than 1
    for i in mp:
        if mp[i] > 1:
            print(i)


# Example 1
one, two, three, four, two1, four2, four3 = Node(1), Node(2), Node(3), Node(4), Node(2), Node(4), Node(4)
one.left = two
two.left = four
three.left = two1
two1.left = four3
one.right = three
three.right = four2
find_duplicate_subtrees(one)
print()

# Example 2
five, four, six, three, four2, three2, six2 = Node(5), Node(4), Node(6), Node(3), Node(4), Node(3), Node(6)
five.left = four
four.left = three
four2.left = three2
five.right = six
four.right = four2
four2.right = six2
find_duplicate_subtrees(five)