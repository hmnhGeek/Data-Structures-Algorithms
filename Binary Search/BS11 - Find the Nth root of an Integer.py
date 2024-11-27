class Solution:
    @staticmethod
    def _pow(x, n):
        prod = 1
        for i in range(n):
            prod = prod * x
        return prod

    @staticmethod
    def get_nth_root(x, n: int):
        if n <= 0:
            return -1
        if x < 0:
            return -1

        low, high = 0, x
        while low <= high:
            mid = int(low + (high - low)/2)
            possible_ans = Solution._pow(mid, n)
            if possible_ans == x:
                return mid
            if possible_ans < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1


print(Solution.get_nth_root(69, 4))
print(Solution.get_nth_root(27, 3))
print(Solution.get_nth_root(14, 1))
print(Solution.get_nth_root(1000, 3))
print(Solution.get_nth_root(625, 4))