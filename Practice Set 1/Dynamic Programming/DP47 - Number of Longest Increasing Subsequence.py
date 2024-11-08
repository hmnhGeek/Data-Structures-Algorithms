from typing import List


class Solution:
    @staticmethod
    def get_number_of_lis(arr: List[int]) -> int:
        n = len(arr)
        dp = {i: 1 for i in range(len(arr))}
        counts = {i: 1 for i in range(len(arr))}
        for index in range(n):
            for prev in range(index):
                if arr[index] > arr[prev]:
                    if dp[index] < 1 + dp[prev]:
                        dp[index] = 1 + dp[prev]
                        counts[index] = counts[prev]
                    elif dp[index] == 1 + dp[prev]:
                        counts[index] += counts[prev]

        lis_length = max(dp.values())
        num_lis = 0
        for i in dp:
            if dp[i] == lis_length:
                num_lis += counts[i]
        return num_lis


print(Solution.get_number_of_lis([50, 3, 90, 60, 80]))
print(Solution.get_number_of_lis([3, 7, 4, 6]))
print(Solution.get_number_of_lis([5, 7, 2, 3]))
print(Solution.get_number_of_lis([1, 5, 4, 3, 2, 6, 7, 10, 8, 9]))
print(Solution.get_number_of_lis([1, 3, 5, 4, 7]))