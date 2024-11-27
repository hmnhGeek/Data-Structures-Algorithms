class Solution:
    @staticmethod
    def find_square_root(x):
        low, high = 0, x
        while low <= high:
            mid = int(low + (high - low)/2)
            if mid * mid == x:
                return mid
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high


print(Solution.find_square_root(30))
print(Solution.find_square_root(25))
print(Solution.find_square_root(35))
print(Solution.find_square_root(6))
print(Solution.find_square_root(100))