class Solution:
    @staticmethod
    def get_factorial(n):
        result = [1]
        while n != 1:
            result = Solution._multiply(result, n)
            n -= 1
        return result[-1:-len(result)-1:-1]

    @staticmethod
    def _multiply(arr, n):
        temp = [i for i in arr]
        carry = 0
        for i in range(len(arr)):
            mul = (arr[i] * n) + carry
            temp[i] = mul % 10
            carry = mul // 10
        arr = [i for i in temp]
        while carry != 0:
            arr.append(carry % 10)
            carry //= 10
        return arr


print(Solution.get_factorial(5))