# Problem link - https://www.geeksforgeeks.org/problems/smallest-factorial-number5929/1


from math import floor, factorial


class Solution:
    @staticmethod
    def _get_zeros(n):
        """
            This takes O(log5(n)) time and O(1) space.
        """
        count = 0
        power = 1
        while floor(n/(5**power)) > 0:
            count += floor(n/(5**power))
            power += 1
        return count

    @staticmethod
    def get_smallest_factorial(n):
        """
            Overall time complexity is O(log2(n) * log5(n)) and space complexity is O(1).
        """

        # this search space is given in problem.
        low, high = 1, 10000
        while low <= high:
            # assume mid to be the least number having n trailing zeros.
            mid = int(low + (high - low)/2)
            # count the actual trailing zeros in its factorial
            zeros = Solution._get_zeros(mid)

            # if zeros >= n, let's try for lower number
            if zeros >= n:
                high = mid - 1
            else:
                # else try for larger number
                low = mid + 1
        return factorial(low - 1), low, factorial(low)


print(Solution.get_smallest_factorial(1))
print(Solution.get_smallest_factorial(6))
print(Solution.get_smallest_factorial(3))
print(Solution.get_smallest_factorial(10))
