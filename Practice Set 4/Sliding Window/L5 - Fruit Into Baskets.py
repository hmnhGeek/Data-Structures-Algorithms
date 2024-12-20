# Problem link - https://leetcode.com/problems/fruit-into-baskets/
# Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5


class Solution:
    @staticmethod
    def fruits_into_baskets(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        left = right = 0
        n = len(arr)

        # define result variables
        longest_length = 0
        start_index = -1

        # define a tracking dictionary
        d = {i: 0 for i in arr}

        # while there is ground to cover.
        while right < n:
            # increment the count of right indexed fruit.
            d[arr[right]] += 1

            # if the number of baskets used is > 2, shrink from left by only 1 unit.
            if sum(1 for v in d.values() if v != 0) > 2:
                d[arr[left]] -= 1
                left += 1

            # if the number of baskets used is within limits, update result variables.
            if sum(1 for v in d.values() if v != 0) <= 2:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index.
            right += 1

        # return the sub-array denoting the collected fruits.
        return arr[start_index:start_index + longest_length] if start_index != -1 else []


print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([1, 1, 2, 3]))
print(Solution.fruits_into_baskets([1, 2, 3, 4]))
