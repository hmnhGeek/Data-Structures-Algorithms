# Problem link - https://leetcode.com/problems/fruit-into-baskets/description/
# Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5


class Solution:
    @staticmethod
    def solve(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        left = right = 0
        n = len(arr)

        # define basket tracker
        d = {i: 0 for i in arr}

        # define max collected fruits and start index for subarray.
        max_collected = 0
        start_index = -1

        # while there is ground to cover.
        while right < n:
            # increment the count of right indexed fruit.
            d[arr[right]] += 1
            # if more than 2 baskets have been used
            if sum(1 for v in d.values() if v != 0) > 2:
                # shrink from left by just 1 unit.
                d[arr[left]] -= 1
                left += 1
            # if baskets are within limits, update result variables
            if sum(1 for v in d.values() if v != 0) <= 2:
                max_collected = max(max_collected, right - left + 1)
                start_index = left
            # increment right
            right += 1
        # return the subarray
        return arr[start_index:start_index + max_collected] if start_index != -1 else []


print(Solution.solve([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.solve([1, 2, 1]))
print(Solution.solve([0, 1, 2, 2]))
print(Solution.solve([1, 2, 3, 2, 2]))
print(Solution.solve([3, 1, 2, 2, 2, 2]))
print(Solution.solve([1, 1, 2, 3]))
print(Solution.solve([1, 2, 3, 4]))
