

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
            if j % weights[0] == 0:
                return (j // weights[0]) * values[0]
            return 0
        left = -1e6
        if weights[i] <= j:
            left = values[i] + solve(weights, values, i, j - weights[i])
        right = solve(weights, values, i - 1, j)
        return max(left, right)

    print(knapsack([2, 4, 6], [5, 11, 13], 10))
    print(knapsack([5, 10, 20], [7, 2, 4], 15))
    print(knapsack([6, 12], [4, 17], 3))
    print(knapsack([1, 50], [1, 30], 100))
    print(knapsack([1, 3, 4, 5], [10, 40, 50, 70], 8))
    print(knapsack([1, 3, 4, 5], [6, 1, 7, 7], 8))
    print(knapsack([2, 3, 4, 5], [6, 8, 7, 100], 1))


def memoized():
    """
        Time complexity is O(n * capacity) and space complexity is O(n + n*capacity).
    """
    def knapsack(weights, values, capacity):
        n = len(weights)
        dp = {i: {j: None for j in range(capacity + 1)} for i in range(n)}
        return solve(weights, values, n - 1, capacity, dp)

    def solve(weights, values, i, j, dp):
        if j == 0:
            return 0
        if i == 0:
            if j % weights[0] == 0:
                return (j // weights[0]) * values[0]
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = -1e6
        if weights[i] <= j:
            left = values[i] + solve(weights, values, i, j - weights[i], dp)
        right = solve(weights, values, i - 1, j, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]

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
