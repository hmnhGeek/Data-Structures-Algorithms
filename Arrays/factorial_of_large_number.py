class Solution:
    @staticmethod
    def _multiply(result, multiplier):
        carry = 0
        for i in range(len(result)):
            x = multiplier * result[i]
            x = x + carry
            result[i] = x % 10
            carry = x // 10
        while carry > 0:
            result.append(carry % 10)
            carry = carry // 10

    @staticmethod
    def get_factorial(n):
        if n < 0:
            return
        result = [1]
        for multiplier in range(2, n + 1):
            Solution._multiply(result, multiplier)
        return result[-1:-len(result)-1:-1]


print(Solution.get_factorial(5))
print(Solution.get_factorial(10))
print(Solution.get_factorial(6))
print(Solution.get_factorial(0))
print(Solution.get_factorial(25))