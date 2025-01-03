# Problem link - https://leetcode.com/problems/fruit-into-baskets/
# Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5


class Solution:
    @staticmethod
    def fruits_into_baskets(arr):
        """
            Time complexity is O(n) and O(1) is space.
        """

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking variables
        d = {i: 0 for i in arr}

        # define result variables
        longest_length = 0
        start_index = -1

        # while there is ground to cover...
        while right < n:
            d[arr[right]] += 1

            # if more than 2 baskets are used, shrink just one unit from left.
            if sum(1 for v in d.values() if v > 0) > 2:
                d[arr[left]] -= 1
                left += 1

            # if baskets are within limit, update the result variables.
            if sum(1 for v in d.values() if v > 0) <= 2:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index.
            right += 1

        # return the subarray.
        return arr[start_index:start_index+longest_length] if start_index != -1 else []


print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([1, 1, 2, 3]))
print(Solution.fruits_into_baskets([1, 2, 3, 4]))
