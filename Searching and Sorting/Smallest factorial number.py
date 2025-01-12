from math import floor, factorial


class Solution:
    @staticmethod
    def _get_zeros(n):
        count = 0
        power = 1
        while floor(n/(5**power)) > 0:
            count += floor(n/(5**power))
            power += 1
        return count

    @staticmethod
    def get_smallest_factorial(n):
        low, high = 1, 10000
        while low <= high:
            mid = int(low + (high - low)/2)
            zeros = Solution._get_zeros(mid)
            if zeros >= n:
                high = mid - 1
            else:
                low = mid + 1
        return factorial(low - 1), low, factorial(low)


print(Solution.get_smallest_factorial(1))
print(Solution.get_smallest_factorial(6))
print(Solution.get_smallest_factorial(3))
print(Solution.get_smallest_factorial(10))