class Solution:
    @staticmethod
    def arithmetic_number(a, b, c):
        return ((b - a)/c) == ((b - a)//c)


print(Solution.arithmetic_number(1, 3, 2))