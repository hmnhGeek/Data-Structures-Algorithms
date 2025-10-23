# Problem link - https://www.naukri.com/code360/problems/nth-root-of-m_1062679
# Solution - https://www.youtube.com/watch?v=rjEJeYCasHs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=12


class Solution:
    @staticmethod
    def _get_flag_value(mid, n, x):
        result = 1
        for i in range(n):
            result = result * mid
            if result > x:
                return 1
        if result == x:
            return 0
        return -1

    @staticmethod
    def nth_root_of_x(x, n):
        """
            Time complexity is O(n * log(x)) and space complexity is O(1).
        """

        low, high = 0, x
        while low <= high:
            mid = int(low + (high - low)/2)
            flag = Solution._get_flag_value(mid, n, x)
            if flag == 0:
                return mid
            if flag == -1:
                low = mid + 1
            else:
                high = mid - 1
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
