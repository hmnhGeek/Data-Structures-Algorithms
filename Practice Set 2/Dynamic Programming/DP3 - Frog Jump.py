# Problem link - https://www.naukri.com/code360/problems/frog-jump_3621012
# Solution - https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=4


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, index):
        if index == 0:
            return 0

        left = 1e6
        if index - 1 >= 0:
            left = abs(arr[index] - arr[index - 1]) + solve(arr, index - 1)
        right = 1e6
        if index - 2 >= 0:
            right = abs(arr[index] - arr[index - 2]) + solve(arr, index - 2)
        return min(left, right)

    def frog_jump(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))
    print(frog_jump([30, 20, 50, 10, 40]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """

    def solve(arr, index, dp):
        if index == 0:
            return 0

        if dp[index] is not None:
            return dp[index]

        left = 1e6
        if index - 1 >= 0:
            left = abs(arr[index] - arr[index - 1]) + solve(arr, index - 1, dp)
        right = 1e6
        if index - 2 >= 0:
            right = abs(arr[index] - arr[index - 2]) + solve(arr, index - 2, dp)
        dp[index] = min(left, right)
        return dp[index]

    def frog_jump(arr):
        n = len(arr)
        dp = {i: None for i in range(n)}
        return solve(arr, n - 1, dp)

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))
    print(frog_jump([30, 20, 50, 10, 40]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """

    def frog_jump(arr):
        n = len(arr)
        dp = {i: 1e6 for i in range(n)}
        dp[0] = 0
        for index in range(1, n):
            left = 1e6
            if index - 1 >= 0:
                left = abs(arr[index] - arr[index - 1]) + dp[index - 1]
            right = 1e6
            if index - 2 >= 0:
                right = abs(arr[index] - arr[index - 2]) + dp[index - 2]
            dp[index] = min(left, right)
        return dp[n - 1]

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))
    print(frog_jump([30, 20, 50, 10, 40]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    def frog_jump(arr):
        n = len(arr)
        prev = 0
        prev2 = 0
        for index in range(1, n):
            left = 1e6
            if index - 1 >= 0:
                left = abs(arr[index] - arr[index - 1]) + prev
            right = 1e6
            if index - 2 >= 0:
                right = abs(arr[index] - arr[index - 2]) + prev2
            curr = min(left, right)
            prev2 = prev
            prev = curr
        return prev

    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))
    print(frog_jump([30, 20, 50, 10, 40]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()