# Problem link - https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
# Solution - https://www.youtube.com/watch?v=rjEJeYCasHs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=12


class Solution:
    @staticmethod
    def _get_flag(x, n, mid):
        product = 1
        for i in range(n):
            product = product * mid
            if product > x:
                return 2
        if product == x:
            return 1
        return 0

    @staticmethod
    def nth_root_of_x(x, n):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define the search space of binary search
        low, high = 0, x
        while low <= high:
            mid = int(low + (high - low)/2)

            # get the flag
            flag = Solution._get_flag(x, n, mid)

            # if flag == 2, then mid^n > x, hence reduce high.
            if flag == 2:
                high = mid - 1

            # if flag == 1, then mid^n == x, hence return mid.
            elif flag == 1:
                return mid

            # else , mid^n < x, hence increase low.
            else:
                low = mid + 1
        return -1


print(Solution.nth_root_of_x(27, 3))
print(Solution.nth_root_of_x(26, 3))
print(Solution.nth_root_of_x(8, 3))
print(Solution.nth_root_of_x(343, 3))
print(Solution.nth_root_of_x(81, 4))
print(Solution.nth_root_of_x(81, 3))
print(Solution.nth_root_of_x(1000, 2))
print(Solution.nth_root_of_x(100, 2))
print(Solution.nth_root_of_x(10**9, 10))
print(Solution.nth_root_of_x(9, 2))
print(Solution.nth_root_of_x(14, 1))
print(Solution.nth_root_of_x(9, 3))
