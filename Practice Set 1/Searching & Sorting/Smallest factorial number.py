# Problem link - https://www.geeksforgeeks.org/problems/smallest-factorial-number5929/1


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
        """
            Overall time complexity is O(log2(n) * log5(n)) and space complexity is O(1).
        """

        # edge case
        if n == 0:
            return 0

        # this search space is given in problem.
        low, high = 1, 10**4
        while low <= high:
            # assume mid to be the least number having n trailing zeros.
            mid = int(low + (high - low)/2)

            # count the actual trailing zeros in its factorial
            num_zeros = Solution._get_num_zeros(mid)

            # if zeros >= n, let's try for lower number
            if num_zeros > n:
                high = mid - 1
            elif num_zeros < n:
                # else try for larger number
                low = mid + 1
            else:
                high = mid - 1
        return low


print(Solution.get_smallest(6))
print(Solution.get_smallest(1))
print(Solution.get_smallest(2))
print(Solution.get_smallest(3))
print(Solution.get_smallest(0))