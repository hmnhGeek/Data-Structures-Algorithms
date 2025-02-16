class Solution:
    @staticmethod
    def find_smallest_subarray_with_sum_gt_k(arr, k):
        left = right = 0
        n = len(arr)
        _sum = 0
        shortest = 1e6
        start_index = -1
        while right < n:
            _sum += arr[right]
            while _sum > k:
                if shortest > right - left + 1:
                    shortest = right - left + 1
                    start_index = left
                _sum -= arr[left]
                left += 1
            right += 1
        return arr[start_index:start_index+shortest] if start_index != -1 else []


print(Solution.find_smallest_subarray_with_sum_gt_k([1, 4, 45, 6, 0, 19], 51))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 100))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 9))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 2, 4], 8))
