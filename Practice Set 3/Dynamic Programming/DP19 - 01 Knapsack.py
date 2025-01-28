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


recursive()
