# Problem link - https://www.naukri.com/code360/problems/partitions-with-given-difference_3751628?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=zoilQD1kYSg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=19


from math import floor


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def get_partition_count(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)
    
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

    print(get_partition_count([1, 2, 2, 3], 3))
    print(get_partition_count([1, 1, 4, 5], 5))
    print(get_partition_count([1, 1, 1], 2))
    print(get_partition_count([2, 34, 5], 40))
    print(get_partition_count([1, 2, 3, 3], 6))
    print(get_partition_count([1, 1, 1, 1], 1))
    print(get_partition_count([5, 2, 3, 10, 6, 8], 10))
    print(get_partition_count([2, 5, 1, 4, 3], 10))
    print(get_partition_count([5, 7, 8], 3))
    print(get_partition_count([35, 2, 8, 22], 0))


def memoized():
    """
        Time complexity is O(n * k) and space complexity is O(n + nk).
    """
    def get_partition_count(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

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

    print(get_partition_count([1, 2, 2, 3], 3))
    print(get_partition_count([1, 1, 4, 5], 5))
    print(get_partition_count([1, 1, 1], 2))
    print(get_partition_count([2, 34, 5], 40))
    print(get_partition_count([1, 2, 3, 3], 6))
    print(get_partition_count([1, 1, 1, 1], 1))
    print(get_partition_count([5, 2, 3, 10, 6, 8], 10))
    print(get_partition_count([2, 5, 1, 4, 3], 10))
    print(get_partition_count([5, 7, 8], 3))
    print(get_partition_count([35, 2, 8, 22], 0))


def tabulation():
    """
        Time complexity is O(n * k) and space complexity is O(nk).
    """
    def get_partition_count(arr, target):
        n = len(arr)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 1
        dp[0][arr[0]] = 1
        for i in range(1, n):
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left + right
        return dp[n - 1][target]

    print(get_partition_count([1, 2, 2, 3], 3))
    print(get_partition_count([1, 1, 4, 5], 5))
    print(get_partition_count([1, 1, 1], 2))
    print(get_partition_count([2, 34, 5], 40))
    print(get_partition_count([1, 2, 3, 3], 6))
    print(get_partition_count([1, 1, 1, 1], 1))
    print(get_partition_count([5, 2, 3, 10, 6, 8], 10))
    print(get_partition_count([2, 5, 1, 4, 3], 10))
    print(get_partition_count([5, 7, 8], 3))
    print(get_partition_count([35, 2, 8, 22], 0))


def space_optimized():
    """
        Time complexity is O(n * k) and space complexity is O(k).
    """
    def get_partition_count(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        prev[arr[0]] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    print(get_partition_count([1, 2, 2, 3], 3))
    print(get_partition_count([1, 1, 4, 5], 5))
    print(get_partition_count([1, 1, 1], 2))
    print(get_partition_count([2, 34, 5], 40))
    print(get_partition_count([1, 2, 3, 3], 6))
    print(get_partition_count([1, 1, 1, 1], 1))
    print(get_partition_count([5, 2, 3, 10, 6, 8], 10))
    print(get_partition_count([2, 5, 1, 4, 3], 10))
    print(get_partition_count([5, 7, 8], 3))
    print(get_partition_count([35, 2, 8, 22], 0))


class Solution:
    @staticmethod
    def _get_partition_count(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        prev[arr[0]] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    @staticmethod
    def count_partition_with_difference(arr, diff):
        """
            Time complexity is O(s^2*n) and space complexity is O(s).
        """
        s = sum(arr)
        count = 0
        for s1 in range(s, -1, -1):
            s2 = s - s1
            if s1 >= s2 and s1 - s2 == diff:
                count += Solution._get_partition_count(arr, s1)
        return count


print(Solution.count_partition_with_difference([5, 2, 6, 4], 3))
print(Solution.count_partition_with_difference([1, 1, 1, 1], 0))
print(Solution.count_partition_with_difference([4, 6, 3], 1))
print(Solution.count_partition_with_difference([3, 1, 1, 2, 1], 0))
print(Solution.count_partition_with_difference([3, 2, 2, 5, 1], 1))
print(Solution.count_partition_with_difference([1, 2, 1, 0, 1, 3, 3], 11))
print(Solution.count_partition_with_difference([1, 2, 3, 1, 2], 1))
