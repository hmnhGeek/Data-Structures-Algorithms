# Problem link - https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=y4vN0WNdrlg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=47


class Solution:
    @staticmethod
    def _longest_increasing_subsequence(arr, dp, parents, n):
        for i in range(n):
            for prev in range(i):
                if arr[prev] < arr[i] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    parents[i] = prev

    @staticmethod
    def _longest_decreasing_subsequence(arr, dp, parents, n):
        for i in range(n - 1, -1, -1):
            for nxt in range(i + 1, n):
                if arr[nxt] < arr[i] and 1 + dp[nxt] > dp[i]:
                    dp[i] = 1 + dp[nxt]
                    parents[i] = nxt

    @staticmethod
    def _get_increasing_part(left, parents1, arr, start_index):
        while parents1[start_index] != start_index:
            left.append(arr[start_index])
            start_index = parents1[start_index]
        left.append(arr[start_index])
        left.reverse()

    @staticmethod
    def _get_decreasing_part(right, parents2, arr, start_index):
        if start_index != parents2[start_index]:
            start_index = parents2[start_index]
            while parents2[start_index] != start_index:
                right.append(arr[start_index])
                start_index = parents2[start_index]
            right.append(arr[start_index])

    @staticmethod
    def longest_bitonic_subsequence(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        n = len(arr)

        # create dp1 and dp2 to store the lengths of LIS. These will take O(n) space.
        dp1 = {i: 1 for i in range(n)}
        dp2 = {i: 1 for i in range(n)}

        # create parents dictionaries to store the parent indices. These will take O(n) space.
        parents1 = {i: i for i in range(n)}
        parents2 = {i: i for i in range(n)}

        # populate dp1, dp2, parents1, parents2 in O(n^2) and O(n) space using the concept of finding LIS.
        Solution._longest_increasing_subsequence(arr, dp1, parents1, n)
        Solution._longest_decreasing_subsequence(arr, dp2, parents2, n)

        # get the lengths of bitonic sequences in O(n) time and O(n) space.
        dp = {i: dp1[i] + dp2[i] - 1 for i in range(n)}

        # store the increasing and decreasing parts in left and right arrays.
        left, right = [], []

        # find the increasing part
        start_index = max(dp, key=dp.get)
        Solution._get_increasing_part(left, parents1, arr, start_index)

        # find the decreasing part
        start_index = max(dp, key=dp.get)
        Solution._get_decreasing_part(right, parents2, arr, start_index)

        # merge and return the longest bitonic subsequence.
        return left + right


print(Solution.longest_bitonic_subsequence([1, 11, 2, 10, 4, 5, 2, 1]))
print(Solution.longest_bitonic_subsequence([1, 2, 1, 2, 1]))
print(Solution.longest_bitonic_subsequence([1, 3, 5, 3, 2]))
print(Solution.longest_bitonic_subsequence([1, 2, 1, 3, 4]))
print(Solution.longest_bitonic_subsequence([12, 11, 40, 5, 3, 1]))
print(Solution.longest_bitonic_subsequence([80, 60, 30]))
print(Solution.longest_bitonic_subsequence([10, 10, 10]))
