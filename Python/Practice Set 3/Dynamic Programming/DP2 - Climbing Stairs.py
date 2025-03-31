# Problem link - https://www.naukri.com/code360/problems/count-ways-to-reach-nth-stairs_798650?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=mLfjzJsN8us&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=3


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(n):
        if n == 0:
            return 1
        left = 0
        if n - 1 >= 0:
            left = solve(n - 1)
        right = 0
        if n - 2 >= 0:
            right = solve(n - 2)
        return left + right

    def climbing_stairs(n):
        return solve(n)

    print(climbing_stairs(3))
    print(climbing_stairs(2))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(n + n).
    """

    def solve(i, dp):
        if i == 0:
            return 1
        if dp[i] is not None:
            return dp[i]
        left = 0
        if i - 1 >= 0:
            left = solve(i - 1, dp)
        right = 0
        if i - 2 >= 0:
            right = solve(i - 2, dp)
        dp[i] = left + right
        return dp[i]

    def climbing_stairs(n):
        dp = {i: None for i in range(n + 1)}
        return solve(n, dp)

    print(climbing_stairs(3))
    print(climbing_stairs(2))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def climbing_stairs(n):
        dp = {i: 0 for i in range(n + 1)}
        dp[0] = 1
        for i in range(1, n + 1):
            left = 0
            if i - 1 >= 0:
                left = dp[i - 1]
            right = 0
            if i - 2 >= 0:
                right = dp[i - 2]
            dp[i] = left + right
        return dp[n]

    print(climbing_stairs(3))
    print(climbing_stairs(2))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def climbing_stairs(n):
        prev = 1
        prev2 = 0
        for i in range(1, n + 1):
            left = 0
            if i - 1 >= 0:
                left = prev
            right = 0
            if i - 2 >= 0:
                right = prev2
            curr = left + right
            prev2 = prev
            prev = curr
        return prev

    print(climbing_stairs(3))
    print(climbing_stairs(2))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(1))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
