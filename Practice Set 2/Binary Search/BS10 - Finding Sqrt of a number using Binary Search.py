# Problem link - https://www.geeksforgeeks.org/square-root-of-an-integer/
# Solution - https://www.youtube.com/watch?v=Bsv3FPUX_BA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=11


class Solution:
    @staticmethod
    def find_sqrt(n):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define a search space from 0 to n
        low, high = 0, n
        while low <= high:
            mid = int(low + (high - low)/2)

            # if n is perfect square of mid, return mid
            if mid * mid == n:
                return mid

            # if mid^2 > n, reduce high
            if mid * mid > n:
                high = mid - 1
            else:
                # else increase low.
                low = mid + 1
        return high


print(Solution.find_sqrt(35))
print(Solution.find_sqrt(100))
print(Solution.find_sqrt(20))
print(Solution.find_sqrt(0))
print(Solution.find_sqrt(625))
