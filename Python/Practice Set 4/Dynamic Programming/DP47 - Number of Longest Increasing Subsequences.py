# Problem link - https://www.naukri.com/code360/problems/number-of-longest-increasing-subsequence_3751627?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=cKVl1TFdNXg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=48


class Solution:
    @staticmethod
    def num_lis(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """
        dp = {i: 1 for i in range(len(arr))}
        count = {i: 1 for i in range(len(arr))}
        for i in range(len(arr)):
            for prev in range(i):
                if arr[prev] < arr[i] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    count[i] = count[prev]
                elif arr[prev] < arr[i] and 1 + dp[prev] == dp[i]:
                    count[i] += count[prev]
        lis_length = max(dp.values())
        count_lis = 0
        for i in dp:
            if dp[i] == lis_length:
                count_lis += count[i]
        return count_lis


print(Solution.num_lis([1, 3, 5, 4, 7]))
print(Solution.num_lis([50, 3, 90, 60, 80]))
print(Solution.num_lis([3, 7, 4, 6]))
print(Solution.num_lis([5, 7, 2, 3]))
print(Solution.num_lis([2, 2, 2, 2, 2]))
print(Solution.num_lis([1, 5, 4, 3, 2, 6, 7, 10, 8, 9]))
