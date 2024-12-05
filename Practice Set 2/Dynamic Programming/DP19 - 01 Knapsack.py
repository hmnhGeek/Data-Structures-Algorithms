def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(weights, cost, index, capacity):
        if index == 0:
            return cost[0] if capacity >= weights[0] else 0
        left = -1e6
        if weights[index] <= capacity:
            left = cost[index] + solve(weights, cost, index - 1, capacity - weights[index])
        right = solve(weights, cost, index - 1, capacity)
        return max(left, right)

    def knapsack(weights, cost, capacity):
        n = len(weights)
        return solve(weights, cost, n - 1, capacity)

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def memoized():
    """
        Time complexity is O(n * capacity) and space complexity is O(n + n * capacity).
    """

    def solve(weights, cost, index, capacity, dp):
        if index == 0:
            return cost[0] if capacity >= weights[0] else 0
        if dp[index][capacity] is not None:
            return dp[index][capacity]
        left = -1e6
        if weights[index] <= capacity:
            left = cost[index] + solve(weights, cost, index - 1, capacity - weights[index], dp)
        right = solve(weights, cost, index - 1, capacity, dp)
        dp[index][capacity] = max(left, right)
        return dp[index][capacity]

    def knapsack(weights, cost, capacity):
        n = len(weights)
        dp = {i: {j: None for j in range(capacity + 1)} for i in range(n)}
        return solve(weights, cost, n - 1, capacity, dp)

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def tabulation():
    """
        Time complexity is O(n * capacity) and space complexity is O(n * capacity).
    """
    def knapsack(weights, cost, capacity):
        n = len(weights)
        dp = {i: {j: 0 for j in range(capacity + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = cost[0] if j >= weights[0] else 0
        for index in range(1, n):
            for cap in range(capacity + 1):
                left = -1e6
                if weights[index] <= cap:
                    left = cost[index] + dp[index - 1][cap - weights[index]]
                right = dp[index - 1][cap]
                dp[index][cap] = max(left, right)
        return dp[n - 1][capacity]

    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))
    print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 5))


def space_optimized():
    """
        Time complexity is O(n * capacity) and space complexity is O(capacity).
    """
    def knapsack(weights, cost, capacity):
        n = len(weights)
        prev = {j: 0 for j in range(capacity + 1)}
        for j in prev:
            prev[j] = cost[0] if j >= weights[0] else 0
        for index in range(1, n):
            curr = {j: 0 for j in range(capacity + 1)}
            for cap in range(capacity + 1):
                left = -1e6
                if weights[index] <= cap:
                    left = cost[index] + prev[cap - weights[index]]
                right = prev[cap]
                curr[cap] = max(left, right)
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
