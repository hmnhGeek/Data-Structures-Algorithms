# Problem link - https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1


class Solution:
    @staticmethod
    def find_smallest_subarray_with_sum_gt_k(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking variables
        _sum = 0

        # define result variables.
        shortest = 1e6
        start_index = -1

        # while there is ground to cover.
        while right < n:
            # add right indexed value
            _sum += arr[right]

            # while the sum is greater than `k`, update the result variables and then shrink from left by one unit.
            while _sum > k:
                if shortest > right - left + 1:
                    shortest = right - left + 1
                    start_index = left
                _sum -= arr[left]
                left += 1

            # increment right index.
            right += 1

        # return the subarray.
        return arr[start_index:start_index+shortest] if start_index != -1 else []


print(Solution.find_smallest_subarray_with_sum_gt_k([1, 4, 45, 6, 0, 19], 51))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 100))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 9))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
print(Solution.find_smallest_subarray_with_sum_gt_k([1, 2, 4], 8))
