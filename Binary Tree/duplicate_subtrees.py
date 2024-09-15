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
            result.append(root)
        mp[subtree_string] += 1
    else:
        mp[subtree_string] = 1

    return subtree_string

def find_duplicate_subtrees(root):
    mp = {}
    result = []
    solve_duplicate_subtrees(root, mp, result)
    return result