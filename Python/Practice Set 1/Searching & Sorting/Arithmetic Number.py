# Problem link - https://www.geeksforgeeks.org/problems/arithmetic-number2815/1


class Solution:
    @staticmethod
    def arithmetic_number(a, b, c):
        """
            Time and space complexities both are O(1).
        """

        return ((b - a)/c) == ((b - a)//c)


print(Solution.arithmetic_number(1, 3, 2))
print(Solution.arithmetic_number(1, 2, 3))
print(Solution.arithmetic_number(1, 2, 4))
