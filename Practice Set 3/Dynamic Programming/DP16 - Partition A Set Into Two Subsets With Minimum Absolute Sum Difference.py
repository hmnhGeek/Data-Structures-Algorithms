# Problem link - https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=GS_OqZb2CWc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=17


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
        Time complexity is O(n * target) and space complexity is O(n + n * target).
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
        Time complexity is O(n * target) and space complexity is O(n * target).
    """
    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: False for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = True
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
        Time complexity is O(n * target) and space complexity is O(target).
    """
    def subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
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
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
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

    @staticmethod
    def min_diff_subset(arr):
        """
            Overall time complexity is O(n * sum^2) and space complexity is O(sum).
        """

        # get the sum of the total array in O(n) time.
        _sum = sum(arr)

        # assume the minimum subset difference to be inf.
        min_diff = 1e6

        # now loop for O(sum//2) time
        for s1 in range(1, _sum//2 + 1):
            # each subset sum check will take O(n * (_sum - s1)) time and O(_sum - s1) space.
            if Solution._subset_sum(arr, _sum - s1):
                min_diff = min(min_diff, abs((_sum - s1) - s1))
        return min_diff


print(Solution.min_diff_subset([1, 2, 3, 4]))
print(Solution.min_diff_subset([3, 1, 5, 2, 8]))
print(Solution.min_diff_subset([8, 6, 5]))
print(Solution.min_diff_subset([3, 9, 7, 3]))
print(Solution.min_diff_subset([1, 6, 11, 5]))
print(Solution.min_diff_subset([1, 5, 11, 5]))
