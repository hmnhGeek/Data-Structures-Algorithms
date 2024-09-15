# Problem link - https://www.geeksforgeeks.org/problems/duplicate-subtrees/1
# Solution - https://www.youtube.com/watch?v=m0dG99f5ct4


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def solve_duplicate_subtrees(root, mp, result):
    if root is None:
        return "N"

    subtree_string = f"{root.data},{solve_duplicate_subtrees(root.left, mp, result)},{solve_duplicate_subtrees(root.right, mp, result)}"

    if subtree_string in mp:
        if mp[subtree_string] == 1:
            result.append(root.data)
        mp[subtree_string] += 1
    else:
        mp[subtree_string] = 1

    return subtree_string


def find_duplicate_subtrees(root):
    mp = {}
    result = []
    solve_duplicate_subtrees(root, mp, result)
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