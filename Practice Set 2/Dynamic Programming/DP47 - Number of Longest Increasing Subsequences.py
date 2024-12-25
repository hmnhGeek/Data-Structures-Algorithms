class Solution:
    @staticmethod
    def num_lis(arr):
        n = len(arr)
        dp = {i: 1 for i in range(n)}
        counts = {i: 1 for i in range(n)}
        for i in range(n):
            for prev in range(i):
                if arr[i] > arr[prev] and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
                    counts[i] = counts[prev]
                elif arr[i] > arr[prev] and dp[i] == 1 + dp[prev]:
                    counts[i] += counts[prev]
        lis_length = max(dp.values())
        nums = 0
        for i in range(n):
            if dp[i] == lis_length:
                nums += counts[i]
        return nums


print(Solution.num_lis([1, 3, 5, 4, 7]))
print(Solution.num_lis([50, 3, 90, 60, 80]))
print(Solution.num_lis([3, 7, 4, 6]))
print(Solution.num_lis([5, 7, 2, 3]))
print(Solution.num_lis([2, 2, 2, 2, 2]))
print(Solution.num_lis([1, 5, 4, 3, 2, 6, 7, 10, 8, 9]))
