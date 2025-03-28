# Problem link - https://www.geeksforgeeks.org/square-root-of-an-integer/
# Solution - https://www.youtube.com/watch?v=Bsv3FPUX_BA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=11


class Solution:
    @staticmethod
    def sqrt(n):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        if n < 0:
            return -1

        # define the search space for binary search
        low, high = 0, n
        while low <= high:
            # get the `mid` value.
            mid = int(low + (high - low)/2)

            # if the mid^2 == n, you can either return mid or increment low to mid + 1 and continue with binary search.
            # Eventually, when the binary search ends, it will end again on this mid-value only.
            if mid**2 == n:
                low = mid + 1

            # if mid^2 > n, we must decrease mid, i.e., decrease high.
            elif mid**2 > n:
                high = mid - 1

            # else, increase low.
            else:
                low = mid + 1

        # return high, which points to the correct square root value.
        return high


print(Solution.sqrt(35))
print(Solution.sqrt(100))
print(Solution.sqrt(20))
print(Solution.sqrt(0))
print(Solution.sqrt(625))
