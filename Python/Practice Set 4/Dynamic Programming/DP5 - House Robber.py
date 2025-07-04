# Problem link - https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=GrMBfJNk_NY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=6


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, i):
        if i < 0:
            return 0
        left = arr[i] + solve(arr, i - 2)
        right = solve(arr, i - 1)
        return max(left, right)

    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """
    def solve(arr, i, dp):
        if i < 0:
            return 0
        if dp[i] is not None:
            return dp[i]
        left = arr[i] + solve(arr, i - 2, dp)
        right = solve(arr, i - 1, dp)
        dp[i] = max(left, right)
        return dp[i]

    def house_robber(arr):
        n = len(arr)
        dp = {i: None for i in range(n)}
        return solve(arr, n - 1, dp)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def house_robber(arr):
        n = len(arr)
        dp = {i: -1e6 for i in range(-2, n)}
        dp[-2] = dp[-1] = 0
        for i in range(n):
            left = arr[i] + dp[i - 2]
            right = dp[i - 1]
            dp[i] = max(left, right)
        return dp[n - 1]

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def house_robber(arr):
        n = len(arr)
        dp = {i: -1e6 for i in range(-2, n)}
        prev2 = prev = 0
        for i in range(n):
            left = arr[i] + prev2
            right = prev
            curr = max(left, right)
            prev2 = prev
            prev = curr
        return prev

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()