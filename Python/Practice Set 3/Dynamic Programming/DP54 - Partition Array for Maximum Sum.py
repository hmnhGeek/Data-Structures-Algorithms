def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, i, k, n):
        if i == n:
            return 0
        max_cost = -1e6
        length = 0
        max_value = -1e6
        for j in range(i, min(n, i + k)):
            length += 1
            max_value = max(max_value, arr[j])
            cost = max_value * length + solve(arr, j + 1, k, n)
            max_cost = max(max_cost, cost)
        return max_cost

    def partition(arr, k):
        n = len(arr)
        return solve(arr, 0, k, n)

    print(partition([1, 15, 7, 9, 2, 5, 10], 3))
    print(partition([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
    print(partition([1], 1))


recursive()
