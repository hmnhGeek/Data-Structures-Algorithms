class Solution:
    @staticmethod
    def kadane(arr):
        curr_sum = 0
        n = len(arr)
        result = -1e6
        for i in range(n):
            curr_sum += arr[i]
            result = max(curr_sum, result)
            if curr_sum < 0:
                curr_sum = 0
        return result


print(Solution.kadane([2, 3, -8, 7, -1, 2, 3]))
print(Solution.kadane([-2, -4]))
print(Solution.kadane([5, 4, 1, 7, 8]))
