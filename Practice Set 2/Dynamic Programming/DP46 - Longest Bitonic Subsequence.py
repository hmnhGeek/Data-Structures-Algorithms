# Problem link - https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=y4vN0WNdrlg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=47


class Solution:
    @staticmethod
    def _front_side(arr):
        n = len(arr)
        dp = {i: 1 for i in range(n)}
        parents = {i: i for i in range(n)}
        for i in range(n):
            for prev in range(i):
                if arr[i] > arr[prev] and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
                    parents[i] = prev
        return dp, parents

    @staticmethod
    def _back_side(arr):
        n = len(arr)
        dp = {i: 1 for i in range(n)}
        parents = {i: i for i in range(n)}
        for i in range(n - 1, -1, -1):
            for prev in range(n - 1, i, -1):
                if arr[i] > arr[prev] and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
                    parents[i] = prev
        return dp, parents

    @staticmethod
    def _construct_increasing_part(arr, start_index, left_slope, parents1):
        while start_index != parents1[start_index]:
            left_slope.append(arr[start_index])
            start_index = parents1[start_index]
        left_slope.append(arr[start_index])
        left_slope = left_slope[-1:-len(left_slope)-1:-1]

    @staticmethod
    def _construct_decreasing_part(arr, start_index, right_slope, parents2):
        while start_index != parents2[start_index]:
            right_slope.append(arr[start_index])
            start_index = parents2[start_index]
        right_slope.append(arr[start_index])

    @staticmethod
    def lbs(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        n = len(arr)

        # in O(n^2) and O(n) space, get the LIS information from left side.
        dp1, parents1 = Solution._front_side(arr)

        # in O(n^2) and O(n) space, get the LIS information from right side.
        dp2, parents2 = Solution._back_side(arr)

        # calculate LBS lengths for each index.
        dp = {i: dp1[i] + dp2[i] - 1 for i in range(n)}

        # store two arrays for storing the left and right parts of the LBS.
        left_slope, right_slope = [], []

        # get the LIS index and construct the increasing part of the LBS
        start_index = max(dp, key=dp.get)
        Solution._construct_increasing_part(arr, start_index, left_slope, parents1)

        # get the LIS index and construct the decreasing part of the LBS
        start_index = max(dp, key=dp.get)
        Solution._construct_decreasing_part(arr, start_index, right_slope, parents2)

        # return the LBS.
        return left_slope + right_slope[1::]


print(Solution.lbs([1, 11, 2, 10, 4, 5, 2, 1]))
print(Solution.lbs([1, 2, 1, 2, 1]))
print(Solution.lbs([1, 3, 5, 3, 2]))
print(Solution.lbs([1, 2, 1, 3, 4]))
print(Solution.lbs([12, 11, 40, 5, 3, 1]))
print(Solution.lbs([80, 60, 30]))
print(Solution.lbs([10, 10, 10]))
