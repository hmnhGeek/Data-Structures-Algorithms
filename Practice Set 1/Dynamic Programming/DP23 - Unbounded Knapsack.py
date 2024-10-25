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


recursive()