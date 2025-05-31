def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i):
        if i == 0:
            return 0
        left = 1e6
        if 0 <= i - 1:
            left = abs(arr[i] - arr[i - 1]) + solve(arr, i - 1)
        right = 1e6
        if 0 <= i - 2:
            right = abs(arr[i] - arr[i - 2]) + solve(arr, i - 2)
        return min(left, right)

    def frog_jump(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(frog_jump([30, 10, 60, 10, 60, 50]))
    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))
    print(frog_jump([30, 20, 50, 10, 40]))


def memoized():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, dp):
        if i == 0:
            return 0
        if dp[i] is not None:
            return dp[i]
        left = 1e6
        if 0 <= i - 1:
            left = abs(arr[i] - arr[i - 1]) + solve(arr, i - 1, dp)
        right = 1e6
        if 0 <= i - 2:
            right = abs(arr[i] - arr[i - 2]) + solve(arr, i - 2, dp)
        dp[i] = min(left, right)
        return dp[i]

    def frog_jump(arr):
        n = len(arr)
        dp = {i: None for i in range(n)}
        return solve(arr, n - 1, dp)

    print(frog_jump([30, 10, 60, 10, 60, 50]))
    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))
    print(frog_jump([30, 20, 50, 10, 40]))


recursive()
print()
memoized()
