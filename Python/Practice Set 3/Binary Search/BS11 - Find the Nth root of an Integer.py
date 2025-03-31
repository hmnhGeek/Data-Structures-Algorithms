# Problem link - https://www.naukri.com/code360/problems/nth-root-of-m_1062679
# Solution - https://www.youtube.com/watch?v=rjEJeYCasHs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=12


class Solution:
    @staticmethod
    def _get_flag(x, mid, n):
        product = 1
        for i in range(n):
            product *= mid
            if product > x:
                return 2
        if product == x:
            return 1
        return 0

    @staticmethod
    def nth_root_of_x(x, n):
        """
            Time complexity is O(n * log(x)) and space complexity is O(1).
        """

        # if either of x or n are negative, then the answer is not possible, return -1.
        if x < 0 or n < 0:
            return -1

        # define a search space.
        low, high = 0, x

        # typical binary search
        while low <= high:
            # get mid-value
            mid = int(low + (high - low)/2)

            # get the flag value in O(n) time.
            flag = Solution._get_flag(x, mid, n)

            # if flag is 2, this means the mid^n > x.
            if flag == 2:
                high = mid - 1

            # if flag == 1, then mid^n = x, return mid.
            elif flag == 1:
                return mid

            # else, increment low.
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
