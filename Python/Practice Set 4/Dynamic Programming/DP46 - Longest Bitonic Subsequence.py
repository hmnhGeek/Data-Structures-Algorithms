class Solution:
    @staticmethod
    def get_longest_bitonic_subsequence(arr):
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


print(Solution.get_longest_bitonic_subsequence([1, 11, 2, 10, 4, 5, 2, 1]))
