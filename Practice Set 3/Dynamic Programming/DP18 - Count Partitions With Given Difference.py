def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, j):
        if j == 0:
            return True
        if i == 0:
            return arr[0] == j
        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

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
    def solve(arr, i, j, dp):
        if j == 0:
            return True
        if i == 0:
            return arr[0] == j
        if dp[i][j] is not None:
            return dp[i][j]
        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left or right
        return dp[i][j]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def tabulation():
    """
        Time complexity is O(n*k) and space complexity is O(nk).
    """
    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: False for j in range(target + 1)} for i in range(n)}

        for i in dp:
            dp[i][0] = True
        if arr[0] in dp[0]:
            dp[0][arr[0]] = True

        for i in range(1, n):
            for j in range(target + 1):
                left = False
                if arr[i] <= j:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left or right
        return dp[n - 1][target]

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def space_optimized():
    """
        Time complexity is O(n*k) and space complexity is O(k).
    """
    def subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}

        prev[0] = True
        if arr[0] in prev:
            prev[arr[0]] = True

        for i in range(1, n):
            curr = {j: False for j in range(target + 1)}
            curr[0] = True
            for j in range(target + 1):
                left = False
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left or right
            prev = curr
        return prev[target]

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


class Solution:
    @staticmethod
    def _subset_sum(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}

        prev[0] = 1
        if arr[0] in prev:
            prev[arr[0]] = 1

        for i in range(1, n):
            curr = {j: False for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = False
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    @staticmethod
    def count_subsets(arr, d):
        s = sum(arr)
        count = 0
        for s1 in range(1, s + 1):
            s2 = s - s1
            if s1 >= s2 and s1 - s2 == d:
                count += Solution._subset_sum(arr, s1)
        return count


print(Solution.count_subsets([5, 2, 6, 4], 3))
print(Solution.count_subsets([1, 1, 1, 1], 0))
print(Solution.count_subsets([4, 6, 3], 1))
print(Solution.count_subsets([3, 1, 1, 2, 1], 0))
print(Solution.count_subsets([3, 2, 2, 5, 1], 1))
print(Solution.count_subsets([1, 2, 1, 0, 1, 3, 3], 11))
print(Solution.count_subsets([1, 2, 3, 1, 2], 1))
