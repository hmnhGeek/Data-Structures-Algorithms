# Problem link - https://www.naukri.com/code360/problems/house-robber_839733?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=3WaxQMELSkw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=7


def recursive():
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
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def memoized():
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
        dp = {i: None for i in range(-2, n)}
        return solve(arr, n - 1, dp)

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def tabulation():
    def house_robber(arr):
        n = len(arr)
        dp = {i: 0 for i in range(-2, n)}
        for index in range(n):
            left = arr[index] + dp[index - 2]
            right = dp[index - 1]
            dp[index] = max(left, right)
        return dp[n - 1]

    print(house_robber([2, 1, 4, 9]))
    print(house_robber([1, 2, 4]))
    print(house_robber([1, 2, 3, 5, 4]))
    print(house_robber([1, 2, 3, 1, 3, 5, 8, 1, 9]))
    print(house_robber([2, 7, 9, 3, 1]))
    print(house_robber([1, 2, 3, 1]))
    print(house_robber([1, 5, 2, 1, 6]))


def space_optimized():
    def house_robber(arr):
        n = len(arr)
        prev2 = prev = 0
        for index in range(n):
            left = arr[index] + prev2
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


class Solution:
    @staticmethod
    def _house_robber(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        n = len(arr)
        prev2 = prev = 0
        for index in range(n):
            left = arr[index] + prev2
            right = prev
            curr = max(left, right)
            prev2 = prev
            prev = curr
        return prev

    @staticmethod
    def house_robber2(arr):
        """
            Time complexity is O(2n) and space complexity is O(2n)
        """
        return max(Solution._house_robber(arr[:-1]), Solution._house_robber(arr[1:]))


print(Solution.house_robber2([2, 3, 2]))
print(Solution.house_robber2([1, 3, 2, 1]))
print(Solution.house_robber2([1, 5, 1, 2, 6]))
print(Solution.house_robber2([2, 3, 5]))
print(Solution.house_robber2([1, 3, 2, 0]))
