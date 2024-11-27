# Problem link - https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
# Solution - https://www.youtube.com/watch?v=rjEJeYCasHs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=12


class Solution:
    @staticmethod
    def _pow(x, n):
        # Time complexity is O(n) and space is O(1).
        prod = 1
        for i in range(n):
            prod = prod * x
        return prod

    @staticmethod
    def get_nth_root(x, n: int):
        # Time complexity is O(n*log(x)) and space complexity is O(1).

        if n <= 0:
            return -1
        if x < 0:
            return -1

        low, high = 0, x
        while low <= high:
            mid = int(low + (high - low)/2)
            # the only change is here... instead of computing simply a square, we raise mid to the power n and
            # then check if the result is equal to x or not. It will take O(n) time.
            possible_ans = Solution._pow(mid, n)
            if possible_ans == x:
                return mid
            if possible_ans < x:
                low = mid + 1
            else:
                high = mid - 1
        # another change is this. In square root problem, we could have simply returned `high` because high^2 was
        # relatively close to x. In case of nth root however, that cannot be a sure case, hence return -1.
        return -1


print(Solution.get_nth_root(69, 4))
print(Solution.get_nth_root(27, 3))
print(Solution.get_nth_root(14, 1))
print(Solution.get_nth_root(1000, 3))
print(Solution.get_nth_root(625, 4))