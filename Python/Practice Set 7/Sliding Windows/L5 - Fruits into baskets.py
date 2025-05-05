# Problem link - https://leetcode.com/problems/fruit-into-baskets/
# Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5


class Solution:
    @staticmethod
    def fruits_into_baskets(arr, k=2):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # define window variables
        n = len(arr)
        left = right = 0

        # define tracking variables
        d = {i: 0 for i in arr}

        # define the resulting variables
        longest_length = 0
        start_index = -1

        # while there is ground to cover...
        while right < n:
            # increment the count of right indexed fruit.
            d[arr[right]] += 1

            # if the distinct fruits breaches k, shrink just 1 unit from left
            if sum(v > 0 for v in d.values()) > k:
                d[arr[left]] -= 1
                left += 1

            # if fruits count is within limit, update the result variables.
            if sum(v > 0 for v in d.values()) <= k:
                if longest_length <= right - left + 1:
                    longest_length = right - left + 1
                    start_index = left

            # increment right index
            right += 1

        # return the sub array.
        return arr[start_index:start_index+longest_length] if start_index != -1 else []


print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([1, 1, 2, 3]))
print(Solution.fruits_into_baskets([1, 2, 3, 4]))
