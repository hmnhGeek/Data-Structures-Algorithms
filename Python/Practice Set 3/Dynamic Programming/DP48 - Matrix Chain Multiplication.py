def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, i, j):
        if i == j:
            return 0
        min_cost = 1e6
        for k in range(i, j):
            cost = arr[i - 1] * arr[k] * arr[j] + solve(arr, i, k) + solve(arr, k + 1, j)
            min_cost = min(cost, min_cost)
        return min_cost

    def mcm(arr):
        n = len(arr)
        return solve(arr, 1, n - 1)

    print(mcm([10, 20, 30, 40, 50]))
    print(mcm([10, 20, 30, 40]))
    print(mcm([4, 5, 3, 2]))
    print(mcm([10, 15, 20, 25]))
    print(mcm([1, 4, 3, 2]))
    print(mcm([2, 1, 3, 4]))
    print(mcm([1, 2, 3, 4, 3]))


recursive()
print()
