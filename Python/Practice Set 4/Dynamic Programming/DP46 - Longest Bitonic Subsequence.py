# Problem link - https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=y4vN0WNdrlg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=47


class Solution:
    @staticmethod
    def longest_bitonic_subsequence(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """
        n = len(arr)
        dp1, parent1 = Solution._get_dp_info(arr, n)
        dp2, parent2 = Solution._get_dp_info(arr[-1:-n-1:-1], n)
        dp2 = dp2[-1:-n-1:-1]
        parent2 = [n - parent2[i] - 1 for i in range(n)][-1:-n-1:-1]
        dp = [dp1[i] + dp2[i] - 1 for i in range(n)]
        max_idx = dp.index(max(dp))
        lis = Solution._get_is(arr, parent1, max_idx)
        dis = Solution._get_ds(arr, parent2, max_idx)
        return lis + dis[1::]

    @staticmethod
    def _get_dp_info(arr, n):
        dp = [1 for i in range(n)]
        parent = [i for i in range(n)]
        for i in range(n):
            for prev in range(i):
                if arr[i] > arr[prev] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    parent[i] = prev
        return dp, parent

    @staticmethod
    def _get_is(arr, parent, max_idx):
        result = []
        start_index = max_idx
        while parent[start_index] != start_index:
            result.append(arr[start_index])
            start_index = parent[start_index]
        result.append(arr[start_index])
        return result[-1:-len(result)-1:-1]

    @staticmethod
    def _get_ds(arr, parent, max_idx):
        result = []
        start_index = max_idx
        while start_index != parent[start_index]:
            result.append(arr[start_index])
            start_index = parent[start_index]
        result.append(arr[start_index])
        return result


print(Solution.longest_bitonic_subsequence([1, 11, 2, 10, 4, 5, 2, 1]))
print(Solution.longest_bitonic_subsequence([1, 2, 1, 2, 1]))
print(Solution.longest_bitonic_subsequence([1, 3, 5, 3, 2]))
print(Solution.longest_bitonic_subsequence([1, 2, 1, 3, 4]))
print(Solution.longest_bitonic_subsequence([12, 11, 40, 5, 3, 1]))
print(Solution.longest_bitonic_subsequence([80, 60, 30]))
print(Solution.longest_bitonic_subsequence([10, 10, 10]))
