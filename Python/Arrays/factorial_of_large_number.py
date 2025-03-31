# Problem link - https://www.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1
# Solution - https://www.youtube.com/watch?v=O3fwYjcMV_M


class Solution:
    @staticmethod
    def _multiply(result, multiplier):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # store a carry as 0.
        carry = 0

        # loop on all the digits of the result
        for i in range(len(result)):
            # get x by multiplying multiplier and result[i]
            x = multiplier * result[i]
            # add any carry into it if needed.
            x = x + carry
            # update ith index with modulo result by 10 as each index can store only a single digit.
            result[i] = x % 10
            # update the carry
            carry = x // 10

        # at the end, if there is any carry, add it to the result as well.
        while carry > 0:
            result.append(carry % 10)
            carry = carry // 10

    @staticmethod
    def get_factorial(n):
        """
            Time complexity is O(n^2) and space complexity is O(m) where m is the number of digits in the n!.
        """

        # edge case
        if n < 0:
            return

        # keep result as 1 for now.
        result = [1]

        # start multiplying till n, starting from 2. This will take O(n^2) time.
        for multiplier in range(2, n + 1):
            Solution._multiply(result, multiplier)

        # return the reverse of the result as the answer.
        return result[-1:-len(result)-1:-1]


print(Solution.get_factorial(5))
print(Solution.get_factorial(10))
print(Solution.get_factorial(6))
print(Solution.get_factorial(0))
print(Solution.get_factorial(25))
