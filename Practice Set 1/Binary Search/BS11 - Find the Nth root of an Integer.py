class Solution:
    @staticmethod
    def nth_root(x, n):
        if x < 0 or n < 0:
            return -1
        low, high = 0, x
        while low <= high:
            mid = int(low + (high - low)/2)
            val = Solution._is_possible(mid, n, x)
            if val == 1:
                return mid
            if val == 2:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    @staticmethod
    def _is_possible(mid, n, x):
        ans = 1
        for i in range(n):
            ans *= mid
            if ans > x:
                return 2
        if ans == x:
            return 1
        return 0


print(Solution.nth_root(81, 4))
print(Solution.nth_root(81, 3))
print(Solution.nth_root(1000, 2))
print(Solution.nth_root(100, 2))
print(Solution.nth_root(10**9, 10))