# Problem link - https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
# Solution - https://www.youtube.com/watch?v=OgvOZ6OrJoY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=24


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(weights, values, index, capacity):
        if capacity == 0:
            return 0

        if index == 0:
            return (capacity // weights[0]) * values[0]

        left = 0
        if weights[index] <= capacity:
            left = values[index] + solve(weights, values, index, capacity - weights[index])
        right = solve(weights, values, index - 1, capacity)
        return max(left, right)

    def unbounded_knapsack(weights, values, capacity):
        n = len(weights)
        return solve(weights, values, n - 1, capacity)

    print(unbounded_knapsack([2, 4, 6], [5, 11, 13], 10))
    print(unbounded_knapsack([5, 10, 20], [7, 2, 4], 15))
    print(unbounded_knapsack([4, 17], [6, 12], 3))


def memoized():
    """
        Time complexity is O(capacity*n) and space complexity is O(n + capacity*n).
    """
    def solve(weights, values, index, capacity, dp):
        if capacity == 0:
            return 0

        if index == 0:
            return (capacity // weights[0]) * values[0]

        if dp[index][capacity] is not None:
            return dp[index][capacity]

        left = 0
        if weights[index] <= capacity:
            left = values[index] + solve(weights, values, index, capacity - weights[index], dp)
        right = solve(weights, values, index - 1, capacity, dp)
        dp[index][capacity] = max(left, right)
        return dp[index][capacity]

    def unbounded_knapsack(weights, values, capacity):
        n = len(weights)
        dp = {i: {j: None for j in range(capacity + 1)} for i in range(n)}
        return solve(weights, values, n - 1, capacity, dp)

    print(unbounded_knapsack([2, 4, 6], [5, 11, 13], 10))
    print(unbounded_knapsack([5, 10, 20], [7, 2, 4], 15))
    print(unbounded_knapsack([4, 17], [6, 12], 3))


def tabulation():
    """
        Time complexity is O(capacity*n) and space complexity is O(capacity*n).
    """
    def unbounded_knapsack(weights, values, capacity):
        n = len(weights)
        dp = {i: {j: 0 for j in range(capacity + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = (j // weights[0]) * values[0]
        for i in dp:
            dp[i][0] = 0

        for index in range(1, n):
            for cap in range(1, capacity + 1):
                left = 0
                if weights[index] <= cap:
                    left = values[index] + dp[index][cap - weights[index]]
                right = dp[index - 1][cap]
                dp[index][cap] = max(left, right)
        return dp[n - 1][capacity]

    print(unbounded_knapsack([2, 4, 6], [5, 11, 13], 10))
    print(unbounded_knapsack([5, 10, 20], [7, 2, 4], 15))
    print(unbounded_knapsack([4, 17], [6, 12], 3))


def space_optimized():
    """
        Time complexity is O(capacity*n) and space complexity is O(capacity).
    """
    def unbounded_knapsack(weights, values, capacity):
        n = len(weights)
        prev = {j: 0 for j in range(capacity + 1)}
        for j in prev:
            prev[j] = (j // weights[0]) * values[0]
        prev[0] = 0

        for index in range(1, n):
            curr = {j: 0 for j in range(capacity + 1)}
            curr[0] = 0
            for cap in range(1, capacity + 1):
                left = 0
                if weights[index] <= cap:
                    left = values[index] + curr[cap - weights[index]]
                right = prev[cap]
                curr[cap] = max(left, right)
            prev = curr
        return prev[capacity]

    print(unbounded_knapsack([2, 4, 6], [5, 11, 13], 10))
    print(unbounded_knapsack([5, 10, 20], [7, 2, 4], 15))
    print(unbounded_knapsack([4, 17], [6, 12], 3))
    print(unbounded_knapsack([1, 50], [1, 30], 100))
    print(unbounded_knapsack([1, 3, 4, 5], [10, 40, 50, 70], 8))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()