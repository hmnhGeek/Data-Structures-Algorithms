class Solution:
    @staticmethod
    def _count_nice_subarray(arr, k):
        if k < 0:
            return 0

        left = right = 0
        n = len(arr)
        odd_num_count = 0
        count_less_than_equal_to_k = 0
        while right < n:
            odd_num_count += (arr[right] % 2)
            while odd_num_count > k:
                odd_num_count -= (arr[left] % 2)
                left += 1
            count_less_than_equal_to_k += (right - left + 1)
            right += 1
        return count_less_than_equal_to_k

    @staticmethod
    def count_nice_subarray(arr, k):
        return Solution._count_nice_subarray(arr, k) - Solution._count_nice_subarray(arr, k - 1)


print(Solution.count_nice_subarray([1, 1, 2, 1, 1], 3))
print(Solution.count_nice_subarray([2, 4, 6], 1))
print(Solution.count_nice_subarray([2,2,2,1,2,2,1,2,2,2], 2))
