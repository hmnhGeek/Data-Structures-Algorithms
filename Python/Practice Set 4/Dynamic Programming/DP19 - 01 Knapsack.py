# Problem link - https://www.naukri.com/code360/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=GqOmJHQZivw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=21


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def knapsack(weights, values, capacity):
        n = len(weights)
        return solve(weights, values, n - 1, capacity)

    def solve(weights, values, i, j):
        if j == 0:
            return 0
        if i == 0:
            return values[0] if weights[0] <= j else 0
        left = 0
        if j >= weights[i]:
            left = values[i] + solve(weights, values, i - 1, j - weights[i])
        right = solve(weights, values, i - 1, j)
        return max(left, right)

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """
    def knapsack(weights, values, capacity):
        n = len(weights)
        dp = {i: {j: None for j in range(capacity + 1)} for i in range(n)}
        return solve(weights, values, n - 1, capacity, dp)

    def solve(weights, values, i, j, dp):
        if j == 0:
            return 0
        if i == 0:
            return values[0] if weights[0] <= j else 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if j >= weights[i]:
            left = values[i] + solve(weights, values, i - 1, j - weights[i], dp)
        right = solve(weights, values, i - 1, j, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def tabulation():
    """
        Time complexity is O(n*k) and space complexity is O(nk).
    """
    def knapsack(weights, values, capacity):
        n = len(weights)
        dp = {i: {j: 0 for j in range(capacity + 1)} for i in range(n)}
        for j in dp[0]:
            if j >= weights[0]:
                dp[0][j] = values[0]
        for i in range(1, n):
            for j in range(capacity + 1):
                left = 0
                if j >= weights[i]:
                    left = values[i] + dp[i - 1][j - weights[i]]
                right = dp[i - 1][j]
                dp[i][j] = max(left, right)
        return dp[n - 1][capacity]

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def space_optimized():
    """
        Time complexity is O(n*k) and space complexity is O(k).
    """
    def knapsack(weights, values, capacity):
        n = len(weights)
        prev = {j: 0 for j in range(capacity + 1)}
        for j in prev:
            if j >= weights[0]:
                prev[j] = values[0]
        for i in range(1, n):
            curr = {j: 0 for j in range(capacity + 1)}
            for j in range(capacity + 1):
                left = 0
                if j >= weights[i]:
                    left = values[i] + prev[j - weights[i]]
                right = prev[j]
                curr[j] = max(left, right)
            prev = curr
        return prev[capacity]

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
print()
