def recursive():
    """
        T: O(2^n) and space is O(n)
    """

    def solve(wt, val, index, cap):
        if index == 0:
            if wt[0] <= cap:
                return val[0]
            else:
                return 0

        left = -1e6
        if wt[index] <= cap:
            left = val[index] + solve(wt, val, index - 1, cap - wt[index])
        right = solve(wt, val, index - 1, cap)
        return max(left, right)

    def knapsack(wt, val, cap):
        n = len(wt)
        return solve(wt, val, n - 1, cap)

    print(knapsack([3, 4, 5], [30, 50, 60], 8))
    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))


def memoized():
    """
        T: O(n*cap) and space is O(n + n*cap)
    """

    def solve(wt, val, index, cap, dp):
        if index == 0:
            if wt[0] <= cap:
                return val[0]
            else:
                return 0

        if dp[index][cap] is not None:
            return dp[index][cap]

        left = -1e6
        if wt[index] <= cap:
            left = val[index] + solve(wt, val, index - 1, cap - wt[index], dp)
        right = solve(wt, val, index - 1, cap, dp)
        dp[index][cap] = max(left, right)
        return dp[index][cap]

    def knapsack(wt, val, cap):
        n = len(wt)
        dp = {i: {j: None for j in range(cap + 1)} for i in range(n)}
        return solve(wt, val, n - 1, cap, dp)

    print(knapsack([3, 4, 5], [30, 50, 60], 8))
    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))


def tabulation():
    """
        T: O(n*cap) and space is O(n*cap)
    """
    def knapsack(wt, val, cap):
        n = len(wt)
        dp = {i: {j: -1e6 for j in range(cap + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = val[0] if wt[0] <= j else 0

        for index in range(1, n):
            for c in range(cap + 1):
                left = -1e6
                if wt[index] <= c:
                    left = val[index] + dp[index - 1][c - wt[index]]
                right = dp[index - 1][c]
                dp[index][c] = max(left, right)
        return dp[n - 1][cap]

    print(knapsack([3, 4, 5], [30, 50, 60], 8))
    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))


def space_optimized():
    """
        T: O(n*cap) and space is O(cap)
    """
    def knapsack(wt, val, cap):
        n = len(wt)
        prev = {j: -1e6 for j in range(cap + 1)}
        for j in prev:
            prev[j] = val[0] if wt[0] <= j else 0

        for index in range(1, n):
            curr = {j: -1e6 for j in range(cap + 1)}
            for c in range(cap + 1):
                left = -1e6
                if wt[index] <= c:
                    left = val[index] + prev[c - wt[index]]
                right = prev[c]
                curr[c] = max(left, right)
            prev = curr
        return prev[cap]

    print(knapsack([3, 4, 5], [30, 50, 60], 8))
    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()