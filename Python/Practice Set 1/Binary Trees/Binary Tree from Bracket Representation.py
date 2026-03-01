class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class IndexTracker:
    def __init__(self):
        self.index = 0


class Utility:
    @staticmethod
    def isdigit(string: str) -> bool:
        try:
            int(string)
            return True
        except:
            return False


class Solution:
    @staticmethod
    def get_binary_tree(string: str) -> Node:
        tracker = IndexTracker()
        return Solution._solve(tracker, string, len(string))

    @staticmethod
    def _solve(tracker: IndexTracker, string: str, n: int) -> Node:
        if tracker.index >= n or string[tracker.index] == ")":
            tracker.index += 1
            return None
        number = 0
        while tracker.index < n and Utility.isdigit(string[tracker.index]):
            number = number*10 + int(string[tracker.index])
            tracker.index += 1
        node = Node(number)
        # construct left tree
        if tracker.index < n and string[tracker.index] == "(":
            tracker.index += 1
            node.left = Solution._solve(tracker, string, n)
        # construct right tree
        if tracker.index < n and string[tracker.index] == "(":
            tracker.index += 1
            node.right = Solution._solve(tracker, string, n)
        tracker.index += 1
        return node
