class Solution:
    @staticmethod
    def sqrt(n):
        low, high = 0, n
        while low <= high:
            mid = int(low + (high - low)/2)
            if mid**2 == n:
                low = mid + 1
            elif mid**2 > n:
                high = mid - 1
            else:
                low = mid + 1
        return high


print(Solution.sqrt(35))