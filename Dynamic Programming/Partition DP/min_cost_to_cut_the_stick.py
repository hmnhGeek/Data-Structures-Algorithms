# Problem link - https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
# Solution - https://www.youtube.com/watch?v=xwomavsC86c&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=51


def recursive():
    # The time complexity will be exponential with O(n) stack space.
    def solve(cuts, i, j):
        # if you've exhausted the rod, return 0.
        if i > j:
            return 0

        mini = float('inf')
        # we start partition from i and go till j (inclusive) because j + 1 represents the end point of rod
        # which we have added manually in the parent function.
        for index in range(i, j + 1):
            # the rod length in which the partition index `index` lies is of length
            # cuts[j + 1] - cuts[i - 1], thus add it to cost and solve for left recursion and right recursion.
            cost = cuts[j + 1] - cuts[i - 1] + solve(cuts, i, index - 1) + solve(cuts, index + 1, j)
            # update the minimum cost
            mini = min(mini, cost)
        # finally return `mini`.
        return mini

    def min_cost(stick_size, cuts):
        n = len(cuts)
        cuts.append(stick_size)
        cuts = [0] + cuts
        # this will take O(nlog(n))
        cuts.sort()
        return solve(cuts, 1, n)

    print(min_cost(7, [1, 3, 4, 5]))
    print(min_cost(9, [5, 6, 1, 4, 2]))


def memoized():
    # The time complexity will be O(n^3) with O(n + n^2) stack space.
    def solve(cuts, i, j, dp):
        # if you've exhausted the rod, return 0.
        if i > j:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        mini = float('inf')
        # we start partition from i and go till j (inclusive) because j + 1 represents the end point of rod
        # which we have added manually in the parent function.
        for index in range(i, j + 1):
            # the rod length in which the partition index `index` lies is of length
            # cuts[j + 1] - cuts[i - 1], thus add it to cost and solve for left recursion and right recursion.
            cost = cuts[j + 1] - cuts[i - 1] + solve(cuts, i, index - 1, dp) + solve(cuts, index + 1, j, dp)
            # update the minimum cost
            mini = min(mini, cost)
        # finally return `mini`.
        dp[i][j] = mini
        return dp[i][j]

    def min_cost(stick_size, cuts):
        n = len(cuts)
        cuts.append(stick_size)
        cuts = [0] + cuts
        # this will take O(nlog(n))
        cuts.sort()

        # using n + 2 in range because we have added 0 and stick_size to the cuts array.
        dp = {i: {j: None for j in range(n + 2)} for i in range(n + 2)}
        return solve(cuts, 1, n, dp)

    print(min_cost(7, [1, 3, 4, 5]))
    print(min_cost(9, [5, 6, 1, 4, 2]))


def tabulation():
    # The time complexity will be O(n^3) with O(n^2) space complexity.

    def min_cost(stick_size, cuts):
        n = len(cuts)
        cuts.append(stick_size)
        cuts = [0] + cuts
        # this will take O(nlog(n))
        cuts.sort()

        # using n + 2 in range because we have added 0 and stick_size to the cuts array.
        dp = {i: {j: 0 for j in range(n + 2)} for i in range(n + 2)}

        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i > j:
                    continue
                mini = float('inf')
                # we start partition from i and go till j (inclusive) because j + 1 represents the end point of rod
                # which we have added manually in the parent function.
                for index in range(i, j + 1):
                    # the rod length in which the partition index `index` lies is of length
                    # cuts[j + 1] - cuts[i - 1], thus add it to cost and solve for left recursion and right recursion.
                    cost = cuts[j + 1] - cuts[i - 1] + dp[i][index - 1] + dp[index + 1][j]
                    # update the minimum cost
                    mini = min(mini, cost)
                # finally return `mini`.
                dp[i][j] = mini
        return dp[1][n]

    print(min_cost(7, [1, 3, 4, 5]))
    print(min_cost(9, [5, 6, 1, 4, 2]))


recursive()
print()
memoized()
print()
tabulation()
