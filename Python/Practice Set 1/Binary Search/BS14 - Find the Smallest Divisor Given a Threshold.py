# Problem link - https://www.naukri.com/code360/problems/smallest-divisor-with-the-given-limit_1755882
# Solution - https://www.youtube.com/watch?v=UvBKTVaG6U8&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=16


from math import ceil


class Solution:
    @staticmethod
    def _threshold_not_breached(arr, mid, threshold):
        val = 0
        for i in range(len(arr)):
            val += ceil(arr[i] / mid)
        return val <= threshold

    @staticmethod
    def find_smallest(arr, threshold):
        """
            Time complexity is O(n*log(max)) and space complexity is O(1).
        """

        # if threshold < length of array, then no divisor can achieve the desired result as any number used as a divisor
        # will yield 1 as quotient only.
        if threshold < len(arr):
            return -1

        # define a search space.
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low) / 2)
            is_possible = Solution._threshold_not_breached(arr, mid, threshold)
            if is_possible:
                # if it is possible to get quotient sum <= threshold with mid, then reduce high to increase quotient sum
                # and check if lower side can give use results as well.
                high = mid - 1
            else:
                # else increase denominator and reduce quotient sum to come within <= threshold.
                low = mid + 1

        # return `low` index which points the correct answer.
        return low


print(Solution.find_smallest([1, 2, 5, 9], 6))
print(Solution.find_smallest([1, 2, 3, 4, 5], 8))
print(Solution.find_smallest([8, 4, 2, 3], 10))
print(Solution.find_smallest([2, 3, 5, 7, 11], 11))
print(Solution.find_smallest([44, 22, 33, 11, 1], 5))
print(Solution.find_smallest([2, 3, 7, 4, 10], 5))
print(Solution.find_smallest([7, 3, 3, 6], 10))
print(Solution.find_smallest([1, 1, 1, 1], 4))
