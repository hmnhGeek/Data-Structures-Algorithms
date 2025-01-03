# Problem link - https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
# Solution - https://www.youtube.com/watch?v=fWX9xDmIzRI&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=15


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, i, k):
        if k == 0:
            return True
        if i == 0:
            return arr[0] == k

        left = False
        if arr[i] <= k:
            left = solve(arr, i - 1, k - arr[i])
        right = solve(arr, i - 1, k)
        return left or right

    def subset_sum(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """

    def solve(arr, i, k, dp):
        if k == 0:
            return True
        if i == 0:
            return arr[0] == k

        if dp[i][k] is not None:
            return dp[i][k]

        left = False
        if arr[i] <= k:
            left = solve(arr, i - 1, k - arr[i], dp)
        right = solve(arr, i - 1, k, dp)
        dp[i][k] = left or right
        return dp[i][k]

    def subset_sum(arr, k):
        n = len(arr)
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        return solve(arr, n - 1, k, dp)

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def tabulation():
    """
        Time complexity is O(n * k) and space complexity is O(n * k).
    """
    def subset_sum(arr, k):
        n = len(arr)
        dp = {i: {j: False for j in range(k + 1)} for i in range(n)}
        for i in range(n):
            dp[i][0] = True
        dp[0][arr[0]] = True
        for i in range(1, n):
            for j in range(k + 1):
                left = False
                if arr[i] <= j:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left or right
        return dp[n - 1][k]

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def space_optimized():
    """
        Time complexity is O(n * k) and space complexity is O(k).
    """
    def subset_sum(arr, k):
        n = len(arr)
        prev = {j: False for j in range(k + 1)}
        prev[arr[0]] = True
        prev[0] = True
        for i in range(1, n):
            curr = {j: False for j in range(k + 1)}
            for j in range(k + 1):
                left = False
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left or right
            prev = curr
        return prev[k]

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
