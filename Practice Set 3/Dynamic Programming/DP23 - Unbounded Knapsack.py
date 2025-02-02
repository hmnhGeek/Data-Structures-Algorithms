def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(wts, vals, i, j):
        if j == 0:
            return 0
        if i == 0:
            return (j // wts[0]) * vals[0]
        left = 0
        if wts[i] <= j:
            left = vals[i] + solve(wts, vals, i, j - wts[i])
        right = solve(wts, vals, i - 1, j)
        return max(left, right)

    def knapsack(wts, vals, capacity):
        n = len(wts)
        return solve(wts, vals, n - 1, capacity)

    print(knapsack([2, 4, 6], [5, 11, 13], 10))
    print(knapsack([5, 10, 20], [7, 2, 4], 15))
    print(knapsack([6, 12], [4, 17], 3))
    print(knapsack([1, 50], [1, 30], 100))
    print(knapsack([1, 3, 4, 5], [10, 40, 50, 70], 8))
    print(knapsack([1, 3, 4, 5], [6, 1, 7, 7], 8))
    print(knapsack([2, 3, 4, 5], [6, 8, 7, 100], 1))


def memoized():
    """
        Time complexity is O(nk) and space complexity is O(n + nk).
    """

    def solve(wts, vals, i, j, dp):
        if j == 0:
            return 0
        if i == 0:
            return (j // wts[0]) * vals[0]
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if wts[i] <= j:
            left = vals[i] + solve(wts, vals, i, j - wts[i], dp)
        right = solve(wts, vals, i - 1, j, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]

    def knapsack(wts, vals, capacity):
        n = len(wts)
        dp = {i: {j: None for j in range(capacity + 1)} for i in range(n)}
        return solve(wts, vals, n - 1, capacity, dp)

    print(knapsack([2, 4, 6], [5, 11, 13], 10))
    print(knapsack([5, 10, 20], [7, 2, 4], 15))
    print(knapsack([6, 12], [4, 17], 3))
    print(knapsack([1, 50], [1, 30], 100))
    print(knapsack([1, 3, 4, 5], [10, 40, 50, 70], 8))
    print(knapsack([1, 3, 4, 5], [6, 1, 7, 7], 8))
    print(knapsack([2, 3, 4, 5], [6, 8, 7, 100], 1))


def tabulation():
    """
        Time complexity is O(nk) and space complexity is O(nk).
    """
    def knapsack(wts, vals, capacity):
        n = len(wts)
        dp = {i: {j: 0 for j in range(capacity + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = (j // wts[0]) * vals[0]
        for i in range(1, n):
            for j in range(capacity + 1):
                left = 0
                if wts[i] <= j:
                    left = vals[i] + dp[i][j - wts[i]]
                right = dp[i - 1][j]
                dp[i][j] = max(left, right)
        return dp[n - 1][capacity]

    print(knapsack([2, 4, 6], [5, 11, 13], 10))
    print(knapsack([5, 10, 20], [7, 2, 4], 15))
    print(knapsack([6, 12], [4, 17], 3))
    print(knapsack([1, 50], [1, 30], 100))
    print(knapsack([1, 3, 4, 5], [10, 40, 50, 70], 8))
    print(knapsack([1, 3, 4, 5], [6, 1, 7, 7], 8))
    print(knapsack([2, 3, 4, 5], [6, 8, 7, 100], 1))


def space_optimized():
    """
        Time complexity is O(nk) and space complexity is O(k).
    """
    def knapsack(wts, vals, capacity):
        n = len(wts)
        prev = {j: 0 for j in range(capacity + 1)}
        for j in prev:
            prev[j] = (j // wts[0]) * vals[0]
        for i in range(1, n):
            curr = {j: 0 for j in range(capacity + 1)}
            for j in range(capacity + 1):
                left = 0
                if wts[i] <= j:
                    left = vals[i] + curr[j - wts[i]]
                right = prev[j]
                curr[j] = max(left, right)
            prev = curr
        return prev[capacity]

    print(knapsack([2, 4, 6], [5, 11, 13], 10))
    print(knapsack([5, 10, 20], [7, 2, 4], 15))
    print(knapsack([6, 12], [4, 17], 3))
    print(knapsack([1, 50], [1, 30], 100))
    print(knapsack([1, 3, 4, 5], [10, 40, 50, 70], 8))
    print(knapsack([1, 3, 4, 5], [6, 1, 7, 7], 8))
    print(knapsack([2, 3, 4, 5], [6, 8, 7, 100], 1))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
