class Solution:
    @staticmethod
    def find_sqrt(n):
        low, high = 0, n
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