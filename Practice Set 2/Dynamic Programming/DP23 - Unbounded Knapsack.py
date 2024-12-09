def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(weights, values, index, capacity):
        if capacity == 0:
            return 0
        if index == 0:
            return (capacity // weights[0]) * values[0]
        left = -1e6
        if weights[index] <= capacity:
            left = values[index] + solve(weights, values, index, capacity - weights[index])
        right = solve(weights, values, index - 1, capacity)
        return max(left, right)

    def knapsack(weights, values, capacity):
        n = len(weights)
        return solve(weights, values, n - 1, capacity)

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

    def solve(weights, values, index, capacity, dp):
        if capacity == 0:
            return 0
        if index == 0:
            return (capacity // weights[0]) * values[0]

        if dp[index][capacity] is not None:
            return dp[index][capacity]

        left = -1e6
        if weights[index] <= capacity:
            left = values[index] + solve(weights, values, index, capacity - weights[index], dp)
        right = solve(weights, values, index - 1, capacity, dp)
        dp[index][capacity] = max(left, right)
        return dp[index][capacity]

    def knapsack(weights, values, capacity):
        n = len(weights)
        dp = {i: {j: None for j in range(capacity + 1)} for i in range(n)}
        return solve(weights, values, n - 1, capacity, dp)

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