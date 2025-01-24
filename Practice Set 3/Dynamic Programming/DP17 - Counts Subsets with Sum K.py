# Problem link - https://www.naukri.com/code360/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=ZHyb-A2Mte4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=18


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        left = 0
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    def count(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """

    def solve(arr, i, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left + right
        return dp[i][j]

    def count(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


def tabulation():
    """
        Time complexity is O(n*k) and space complexity is O(nk).
    """
    def count(arr, target):
        n = len(arr)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 1
        if arr[0] in dp[0]:
            dp[0][arr[0]] = 1
        for i in range(1, n):
            for j in range(1, target + 1):
                left = 0
                if arr[i] <= j:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left + right
        return dp[n - 1][target]

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


def space_optimized():
    """
        Time complexity is O(n*k) and space complexity is O(k).
    """
    def count(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        if arr[0] in prev:
            prev[arr[0]] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(1, target + 1):
                left = 0
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    print(count([1, 2, 2, 3], 3))
    print(count([1, 1, 4, 5], 5))
    print(count([1, 1, 1], 2))
    print(count([2, 34, 5], 40))
    print(count([1, 2, 3, 3], 6))
    print(count([1, 1, 1, 1], 1))
    print(count([5, 2, 3, 10, 6, 8], 10))
    print(count([2, 5, 1, 4, 3], 10))
    print(count([5, 7, 8], 3))
    print(count([35, 2, 8, 22], 0))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
