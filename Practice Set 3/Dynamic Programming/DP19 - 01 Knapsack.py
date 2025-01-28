def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(wts, vals, i, cap):
        if cap == 0:
            return 0
        if i == 0:
            return vals[0] if wts[0] <= cap else 0
        left = 0
        if wts[i] <= cap:
            left = vals[i] + solve(wts, vals, i - 1, cap - wts[i])
        right = solve(wts, vals, i - 1, cap)
        return max(left, right)

    def knapsack(wts, vals, cap):
        n = len(wts)
        return solve(wts, vals, n - 1, cap)

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def memoized():
    """
        Time complexity is O(n*cap) and space complexity is O(n + n * cap).
    """
    def solve(wts, vals, i, cap, dp):
        if cap == 0:
            return 0
        if i == 0:
            return vals[0] if wts[0] <= cap else 0
        if dp[i][cap] is not None:
            return dp[i][cap]
        left = 0
        if wts[i] <= cap:
            left = vals[i] + solve(wts, vals, i - 1, cap - wts[i], dp)
        right = solve(wts, vals, i - 1, cap, dp)
        dp[i][cap] = max(left, right)
        return dp[i][cap]

    def knapsack(wts, vals, cap):
        n = len(wts)
        dp = {i: {j: None for j in range(cap + 1)} for i in range(n)}
        return solve(wts, vals, n - 1, cap, dp)

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def tabulation():
    """
        Time complexity is O(n*cap) and space complexity is O(n * cap).
    """
    def knapsack(wts, vals, cap):
        n = len(wts)
        dp = {i: {j: 0 for j in range(cap + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = vals[0] if wts[0] <= j else 0
        for i in range(1, n):
            for j in range(cap + 1):
                left = 0
                if wts[i] <= j:
                    left = vals[i] + dp[i - 1][j - wts[i]]
                right = dp[i - 1][j]
                dp[i][j] = max(left, right)
        return dp[n - 1][cap]

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def space_optimized():
    """
        Time complexity is O(n*cap) and space complexity is O(cap).
    """
    def knapsack(wts, vals, cap):
        n = len(wts)
        prev = {j: 0 for j in range(cap + 1)}
        for j in prev:
            prev[j] = vals[0] if wts[0] <= j else 0
        for i in range(1, n):
            curr = {j: 0 for j in range(cap + 1)}
            for j in range(cap + 1):
                left = 0
                if wts[i] <= j:
                    left = vals[i] + prev[j - wts[i]]
                right = prev[j]
                curr[j] = max(left, right)
            prev = curr
        return prev[cap]

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
