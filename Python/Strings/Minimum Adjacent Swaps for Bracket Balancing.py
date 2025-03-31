# Problem link - https://www.geeksforgeeks.org/problems/minimum-swaps-for-bracket-balancing2704/1
# Solution - https://www.youtube.com/watch?v=WhMbbnHZpis


class Solution:
    @staticmethod
    def min_swaps(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(string)

        # create utility variables
        opened = closed = min_swaps = unbalanced = 0

        # loop in the string
        for i in range(n):
            # if an opening bracket is found...
            if string[i] == '[':
                opened += 1
                """
                    Since an opening bracket is found, we only swap when unbalanced > 0 
                    because that ensures we are actually correcting an existing imbalance. 
                    If unbalanced == 0, it means the sequence is already balanced up to 
                    that point, so no swap is needed.
                """
                if unbalanced > 0:
                    min_swaps += unbalanced
                    # since balancing is completed, reduce one from unbalanced.
                    unbalanced -= 1
            else:
                # if a closed bracket is found, update the unbalanced amount.
                closed += 1
                unbalanced = closed - opened

        # return the min_swaps.
        return min_swaps


print(Solution.min_swaps("[]][]["))
print(Solution.min_swaps("[][]"))
print(Solution.min_swaps("[[[][][]]]"))
print(Solution.min_swaps("]["))
print(Solution.min_swaps("[]][]["))
print(Solution.min_swaps("]][["))
