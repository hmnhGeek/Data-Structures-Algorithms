from math import floor

class Solution:
    @staticmethod
    def _get_num_zeros(mid):
        pow = 1
        count = 0
        while floor(mid/(5**pow)) != 0:
            count += floor(mid/(5**pow))
            pow += 1
        return count

    @staticmethod
    def get_smallest(n):
        low, high = 1, 10**4
        while low <= high:
            mid = int(low + (high - low)/2)
            num_zeros = Solution._get_num_zeros(mid)
            if num_zeros > n:
                high = mid - 1
            elif num_zeros < n:
                low = mid + 1
            else:
                high = mid - 1
        return low


print(Solution.get_smallest(6))
print(Solution.get_smallest(1))