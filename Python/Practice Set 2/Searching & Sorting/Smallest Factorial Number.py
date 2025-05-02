from math import log, ceil, floor


class Solution:
    @staticmethod
    def _get_trailing_zeros_count(mid):
        up_limit = ceil(log(mid, 5))
        trailing_zeros = 0
        for i in range(1, up_limit):
            trailing_zeros += floor(mid/5**i)
        return trailing_zeros

    @staticmethod
    def get_smallest_factorial_number(num_trailing_zeros):
        if num_trailing_zeros < 0:
            return -1
        low, high = 1, 10**4
        while low <= high:
            mid = int(low + (high - low)/2)
            trailing_zeros = Solution._get_trailing_zeros_count(mid)
            if trailing_zeros > num_trailing_zeros:
                high = mid - 1
            elif trailing_zeros == num_trailing_zeros:
                high = mid - 1
            else:
                low = mid + 1
        return high


print(Solution.get_smallest_factorial_number(1))
print(Solution.get_smallest_factorial_number(6))