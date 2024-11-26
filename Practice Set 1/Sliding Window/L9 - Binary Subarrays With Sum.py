class Solution:
    @staticmethod
    def _binary_sum_subarray(arr, k):
        if k < 0:
            return 0
        left = right = 0
        n = len(arr)
        count_less_than_equal_to_k = 0
        window_sum = 0
        while right < n:
            window_sum += arr[right]
            while window_sum > k:
                window_sum -= arr[left]
                left += 1
            count_less_than_equal_to_k += (right - left + 1)
            right += 1
        return count_less_than_equal_to_k

    @staticmethod
    def binary_sum_subarray(arr, k):
        return Solution._binary_sum_subarray(arr, k) - Solution._binary_sum_subarray(arr, k - 1)


print(Solution.binary_sum_subarray([1, 0, 1, 0, 1], 2))
print(Solution.binary_sum_subarray([0]*5, 0))