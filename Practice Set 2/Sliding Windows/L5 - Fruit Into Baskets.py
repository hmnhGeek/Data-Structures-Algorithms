# Problem link - https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/0
# Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5


class Solution:
    @staticmethod
    def fruits_into_baskets(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        n = len(arr)
        left = right = 0
        max_fruits = 0
        start_index = -1

        # define a map to track the baskets
        d = {i: 0 for i in arr}

        # while there is ground to cover.
        while right < n:
            # increment the count of right indexed fruit
            d[arr[right]] += 1

            # if the used baskets is more than 2, shrink just once from the left
            if sum(1 for v in d.values() if v != 0) > 2:
                d[arr[left]] -= 1
                left += 1

            # if the used baskets have become <= 2, update max fruits and start index.
            if sum(1 for v in d.values() if v != 0) <= 2:
                max_fruits = max(max_fruits, right - left + 1)
                start_index = left

            # increment right
            right += 1

        # return the collected fruits sub-array.
        return arr[start_index:start_index + max_fruits]


print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
