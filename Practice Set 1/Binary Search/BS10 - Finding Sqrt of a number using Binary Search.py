class Solution:
    @staticmethod
    def get_sqrt(n):
        if n < 0:
            return -1
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


print(Solution.get_sqrt(30))
print(Solution.get_sqrt(49))
print(Solution.get_sqrt(0))
print(Solution.get_sqrt(10))
print(Solution.get_sqrt(625))
print(Solution.get_sqrt(1000000))