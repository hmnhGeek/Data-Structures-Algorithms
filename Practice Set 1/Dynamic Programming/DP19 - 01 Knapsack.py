def recursive():
    """
        T: O(2^n) and space is O(n)
    """

    def solve(wt, val, index, cap):
        if index == 0:
            if wt[0] <= cap:
                return val[0]
            else:
                return 0

        left = -1e6
        if wt[index] <= cap:
            left = val[index] + solve(wt, val, index - 1, cap - wt[index])
        right = solve(wt, val, index - 1, cap)
        return max(left, right)

    def knapsack(wt, val, cap):
        n = len(wt)
        return solve(wt, val, n - 1, cap)

    print(knapsack([3, 4, 5], [30, 50, 60], 8))
    print(knapsack([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack([4, 5, 1], [1, 2, 3], 4))
    print(knapsack([4, 5, 6], [1, 2, 3], 3))


recursive()