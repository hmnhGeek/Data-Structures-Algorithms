class Solution:
    @staticmethod
    def _count_less_than(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # edge case
        if k < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking variables
        _sum = count = 0

        # while there is ground to cover.
        while right < n:
            # update sum
            _sum += arr[right]

            # shrink continuously from left till the sum > k
            while _sum > k:
                _sum -= arr[left]
                left += 1

            # update the count of subarrays whose sum <= k.
            if _sum <= k:
                count += (right - left + 1)
            right += 1

        # return the count.
        return count

    @staticmethod
    def bin_subarray_count(arr, k):
        return Solution._count_less_than(arr, k) - Solution._count_less_than(arr,  k - 1)


print(Solution.bin_subarray_count([1, 0, 1, 0, 1], 2))
print(Solution.bin_subarray_count([0, 0, 0, 0, 0], 0))
print(Solution.bin_subarray_count([1, 0, 1, 1, 0, 1], 2))
print(Solution.bin_subarray_count([1, 1, 0, 1, 1], 5))
print(Solution.bin_subarray_count([1, 0, 1, 1, 1, 0, 1], 3))
