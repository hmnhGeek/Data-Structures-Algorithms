# Problem link - https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
# Solution - https://www.youtube.com/watch?v=rjEJeYCasHs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=12


class Solution:
    @staticmethod
    def nth_root(x, n):
        """
            Time complexity is O(n*log(x)) and space complexity is O(1).
        """

        # if x is negative or nth root is <= 0, return -1 (Edge Case).
        if x < 0 or n <= 0:
            return -1

        # define a search space.
        low, high = 0, x

        # binary search
        while low <= high:
            mid = int(low + (high - low)/2)

            # if mid as an answer is possible, we will get three types of results
            # 1: if val == 1, it means mid^n = x, return mid
            # 2: if val == 0, it means mid^n < x, increase low
            # 3: if val == 2, it means mid^n > x, reduce high
            val = Solution._is_possible(mid, n, x)
            if val == 1:
                return mid
            if val == 2:
                high = mid - 1
            else:
                low = mid + 1

        # if no perfect nth root is found, return -1.
        return -1

    @staticmethod
    def _is_possible(mid, n, x):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        ans = 1
        for i in range(n):
            ans *= mid
            # if at any point, the answer exceeds x, return 2.
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
print(Solution.nth_root(9, 2))
print(Solution.nth_root(14, 1))
print(Solution.nth_root(9, 3))