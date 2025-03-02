class Solution:
    @staticmethod
    def min_swaps(string):
        n = len(string)
        opened = closed = min_swaps = unbalanced = 0
        for i in range(n):
            if string[i] == '[':
                opened += 1
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