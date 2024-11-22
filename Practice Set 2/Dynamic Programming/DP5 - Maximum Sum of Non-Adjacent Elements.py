# Problem link - https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=GrMBfJNk_NY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=6


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, index):
        if index < 0:
            return 0
        left = arr[index] + solve(arr, index - 2)
        right = solve(arr, index - 1)
        return max(left, right)

    def house_robber(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2,7,9,3,1]))
    print(house_robber([1,2,3,1]))
    print(house_robber([1, 5, 2, 1, 6]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """

    def solve(arr, index, dp):
        if index < 0:
            return 0
        if dp[index] is not None:
            return dp[index]
        left = arr[index] + solve(arr, index - 2, dp)
        right = solve(arr, index - 1, dp)
        dp[index] = max(left, right)
        return dp[index]

    def house_robber(arr):
        n = len(arr)
        dp = {i: None for i in range(n)}
        dp[-1] = dp[-2] = None
        return solve(arr, n - 1, dp)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2,7,9,3,1]))
    print(house_robber([1,2,3,1]))
    print(house_robber([1, 5, 2, 1, 6]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def house_robber(arr):
        n = len(arr)
        dp = {i: 0 for i in range(n)}
        dp[-1] = dp[-2] = 0
        for index in range(n):
            left = arr[index] + dp[index - 2]
            right = dp[index - 1]
            dp[index] = max(left, right)
        return dp[n - 1]

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2,7,9,3,1]))
    print(house_robber([1,2,3,1]))
    print(house_robber([1, 5, 2, 1, 6]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def house_robber(arr):
        n = len(arr)
        prev1 = prev2 = 0
        for index in range(n):
            left = arr[index] + prev2
            right = prev1
            curr = max(left, right)
            prev2 = prev1
            prev1 = curr
        return prev1

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2,7,9,3,1]))
    print(house_robber([1,2,3,1]))
    print(house_robber([1, 5, 2, 1, 6]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()