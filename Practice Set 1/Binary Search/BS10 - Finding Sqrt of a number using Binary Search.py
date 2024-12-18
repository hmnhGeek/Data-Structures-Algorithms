class Solution:
    @staticmethod
    def get_sqrt(n):
        # if the number is negative, no square root can be found.
        if n < 0:
            return -1

        # define a search space.
        low, high = 0, n

        # typical binary search
        while low <= high:
            mid = int(low + (high - low)/2)

            # if mid is the exact square root of n, return it directly.
            if mid * mid == n:
                return mid

            # if mid^2 > n, we are way higher, reduce the search space to left side.
            if mid * mid > n:
                high = mid - 1
            else:
                # if mid^2 < n, we are way lower, reduce the search space to right side.
                low = mid + 1

        # high will point to the correct square root value.
        return high


print(Solution.get_sqrt(30))
print(Solution.get_sqrt(49))
print(Solution.get_sqrt(0))
print(Solution.get_sqrt(10))
print(Solution.get_sqrt(625))
print(Solution.get_sqrt(1000000))