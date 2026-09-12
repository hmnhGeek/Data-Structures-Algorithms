# Problem link - https://www.geeksforgeeks.org/square-root-of-an-integer/
# Solution - https://www.youtube.com/watch?v=Bsv3FPUX_BA&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=11


class Solution:
    @staticmethod
    def find_sqrt(n):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        if n < 0:
            return
        if n == 0:
            return 0
        low, high = 1, n
        while low <= high:
            mid = int(low + (high - low)/2)
            if mid * mid == n:
                return mid
            if mid * mid > n:
                high = mid - 1
            else:
                low = mid + 1
        return high


print(Solution.find_sqrt(35))
print(Solution.find_sqrt(100))
print(Solution.find_sqrt(20))
print(Solution.find_sqrt(0))
print(Solution.find_sqrt(625))