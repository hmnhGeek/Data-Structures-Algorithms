def recursive():
    def solve(arr, index, prev_val):
        """
            Time complexity is O(2^n) and space complexity is O(n).
        """

        if index < 0:
            return 0

        left = -1e6
        if arr[index] < prev_val:
            left = 1 + solve(arr, index - 1, arr[index])
        right = solve(arr, index - 1, prev_val)
        return max(left, right)

    def get_lis(arr):
        n = len(arr)
        return solve(arr, n - 1, 1e6)

    print(get_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis([5, 4, 11, 1, 16, 8]))
    print(get_lis([1, 2, 2]))
    print(get_lis([3, 10, 2, 1, 20]))
    print(get_lis([30, 20, 10]))
    print(get_lis([2, 2, 2]))
    print(get_lis([10, 20, 35, 80]))


def memoized():
    def solve(arr, index, prev_val, dp):
        """
            Time complexity is O(n^2) and space complexity is O(n + n^2).
        """

        if index == 0:
            return 0

        if dp[index][prev_val] is not None:
            return dp[index][prev_val]

        left = -1e6
        if arr[index - 1] < prev_val:
            left = 1 + solve(arr, index - 1, arr[index - 1], dp)
        right = solve(arr, index - 1, prev_val, dp)
        dp[index][prev_val] = max(left, right)
        return dp[index][prev_val]

    def get_lis(arr):
        n = len(arr)
        dp = {i: {j: None for j in arr} for i in range(n + 1)}
        for i in dp:
            dp[i][1e6] = None

        return solve(arr, n, 1e6, dp)

    print(get_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis([5, 4, 11, 1, 16, 8]))
    print(get_lis([1, 2, 2]))
    print(get_lis([3, 10, 2, 1, 20]))
    print(get_lis([30, 20, 10]))
    print(get_lis([2, 2, 2]))
    print(get_lis([10, 20, 35, 80]))


recursive()
print()
memoized()