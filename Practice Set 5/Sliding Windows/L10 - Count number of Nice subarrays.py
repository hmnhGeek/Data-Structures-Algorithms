class Solution:
    @staticmethod
    def _count_less_than_equal_to(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # if k is negative, return 0.
        if k < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking and result variables.
        _sum = count = 0

        # while there is ground to cover.
        while right < n:
            # add 1 if right value is odd, else add 0
            _sum += arr[right] % 2

            # if odd numbers exceed k, continuously shrink from left
            while _sum > k:
                _sum -= arr[left] % 2
                left += 1

            # if odd count is with k, update the count.
            if _sum <= k:
                count += (right - left + 1)

            # increment right index
            right += 1

        # finally, return the count
        return count

    @staticmethod
    def get_nice_subarray_count(arr, k):
        """
            Overall time complexity is O(2n) and space complexity is O(1).
        """

        return Solution._count_less_than_equal_to(arr, k) - Solution._count_less_than_equal_to(arr, k - 1)


print(Solution.get_nice_subarray_count([1, 5, 2, 1, 1], 3))
print(Solution.get_nice_subarray_count([2, 4, 6], 1))
print(Solution.get_nice_subarray_count([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.get_nice_subarray_count([2, 5, 6, 9], 2))
print(Solution.get_nice_subarray_count([2, 2, 5, 6, 9, 2, 11], 2))
