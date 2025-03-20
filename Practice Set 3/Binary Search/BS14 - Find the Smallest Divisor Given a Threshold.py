from math import ceil


class Solution:
    @staticmethod
    def _divide(arr, mid, n):
        value = 0
        for i in range(n):
            value += ceil(arr[i]/mid)
        return value

    @staticmethod
    def smallest_divisor(arr, threshold):
        n = len(arr)

        # if the threshold is less than n, then the answer is not possible because each element would contribute 1 as a
        # quotient at least.
        if threshold < n:
            return -1

        # define the range
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)

            # find the sum of ceiled quotients in O(n) time.
            value = Solution._divide(arr, mid, n)

            # if value <= threshold, we can try for even smaller divisor.
            if value <= threshold:
                high = mid - 1
            else:
                # else we must increase the divisor to decrease the sum of quotient in order to make it smaller than the
                # threshold value.
                low = mid + 1

        # low will point to the correct answer.
        return low


print(Solution.smallest_divisor([1, 2, 5, 9], 6))
print(Solution.smallest_divisor([1, 2, 3, 4, 5], 8))
print(Solution.smallest_divisor([8, 4, 2, 3], 10))
print(Solution.smallest_divisor([2, 3, 5, 7, 11], 11))
print(Solution.smallest_divisor([44, 22, 33, 11, 1], 5))
print(Solution.smallest_divisor([1, 1, 1, 1], 4))
