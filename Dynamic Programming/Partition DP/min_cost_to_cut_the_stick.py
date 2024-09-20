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


recursive()
