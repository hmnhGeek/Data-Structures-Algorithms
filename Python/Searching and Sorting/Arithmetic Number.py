# Problem link - https://www.geeksforgeeks.org/problems/arithmetic-number2815/1


class Solution:
    @staticmethod
    def is_ap_no(a, b, c):
        """
            Time complexity is O(1) and space complexity is O(1).
        """

        res = (b - a)/c + 1
        return int(res) == res


print(Solution.is_ap_no(1, 3, 2))
print(Solution.is_ap_no(1, 2, 3))
print(Solution.is_ap_no(1, 2, 4))
