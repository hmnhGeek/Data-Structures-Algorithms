class Solution:
    @staticmethod
    def min_swaps(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(string)
        opened = closed = min_swaps = unbalanced = 0
        for i in range(n):
            if string[i] == '[':
                opened += 1
                """
                    We only swap when unbalanced > 0 because that ensures we are actually 
                    correcting an existing imbalance. If unbalanced == 0, it means the 
                    sequence is already balanced up to that point, so no swap is needed.
                """
                if unbalanced > 0:
                    min_swaps += unbalanced
                    unbalanced -= 1
            else:
                closed += 1
                unbalanced = closed - opened
        return min_swaps


print(Solution.min_swaps("[]][]["))
print(Solution.min_swaps("[][]"))
print(Solution.min_swaps("[[[][][]]]"))