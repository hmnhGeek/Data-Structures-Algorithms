# Problem link - https://www.naukri.com/code360/problems/smallest-divisor-with-the-given-limit_1755882
# Solution - https://www.youtube.com/watch?v=UvBKTVaG6U8&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=15


import math


class Solution:
    @staticmethod
    def _is_possible(arr, mid, threshold):
        """ Time complexity is O(n) and space complexity is O(1). """
        # get the sum of quotient using a for loop.
        _sum = 0
        for i in range(len(arr)):
            _sum += math.ceil(arr[i] / mid)
        # return if quotient sum <= threshold.
        return _sum <= threshold

    @staticmethod
    def smallest_divisor(arr, threshold):
        """
            Time complexity is O(n * log(max(arr))) and space complexity is O(1).
        """

        # high should be set to max because that will give 1 for all array elements.
        low = 1
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low) / 2)
            is_possible = Solution._is_possible(arr, mid, threshold)

            # if the quotient sum <= threshold, lets decrease the divisor further to increase quotient sum? Let's check
            # how far we can go.
            if is_possible:
                high = mid - 1
            else:
                # if the sum of quotients > threshold, then we must increase the denominator to decrease quotient sum.
                low = mid + 1

        # return `low` which represents the least divisor required by the question.
        return low


print(Solution.smallest_divisor([1, 2, 5, 9], 6))
print(Solution.smallest_divisor([1, 2, 3, 4, 5], 8))
print(Solution.smallest_divisor([8, 4, 2, 3], 10))
print(Solution.smallest_divisor([2, 3, 5, 7, 11], 11))
print(Solution.smallest_divisor([44, 22, 33, 11, 1], 5))
print(Solution.smallest_divisor([1, 1, 1, 1], 4))
