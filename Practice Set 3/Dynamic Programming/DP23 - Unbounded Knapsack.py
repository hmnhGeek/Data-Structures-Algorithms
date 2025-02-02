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


recursive()
print()