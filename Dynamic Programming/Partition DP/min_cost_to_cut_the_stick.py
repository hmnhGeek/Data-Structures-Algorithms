# Problem link - https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
# Solution - https://www.youtube.com/watch?v=xwomavsC86c&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=51


def recursive():
    def solve(cuts, i, j):
        if i > j:
            return 0

        mini = float('inf')
        for index in range(i, j + 1):
            cost = cuts[j + 1] - cuts[i - 1] + solve(cuts, i, index - 1) + solve(cuts, index + 1, j)
            mini = min(mini, cost)
        return mini

    def min_cost(stick_size, cuts):
        n = len(cuts)
        cuts.append(stick_size)
        cuts = [0] + cuts
        cuts.sort()
        return solve(cuts, 1, n)

    print(min_cost(7, [1, 3, 4, 5]))
    print(min_cost(9, [5, 6, 1, 4, 2]))


recursive()
