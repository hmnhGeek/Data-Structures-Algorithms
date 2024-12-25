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
        n = len(arr)
        dp1, parents1 = Solution._front_side(arr)
        dp2, parents2 = Solution._back_side(arr)
        dp = {i: dp1[i] + dp2[i] - 1 for i in range(n)}
        start_index = max(dp, key=dp.get)
        left_slope, right_slope = [], []
        Solution._construct_increasing_part(arr, start_index, left_slope, parents1)
        start_index = max(dp, key=dp.get)
        Solution._construct_decreasing_part(arr, start_index, right_slope, parents2)
        return left_slope + right_slope[1::]


print(Solution.lbs([1, 11, 2, 10, 4, 5, 2, 1]))
print(Solution.lbs([1, 2, 1, 2, 1]))
print(Solution.lbs([1, 3, 5, 3, 2]))
print(Solution.lbs([1, 2, 1, 3, 4]))
print(Solution.lbs([12, 11, 40, 5, 3, 1]))
print(Solution.lbs([80, 60, 30]))
print(Solution.lbs([10, 10, 10]))
