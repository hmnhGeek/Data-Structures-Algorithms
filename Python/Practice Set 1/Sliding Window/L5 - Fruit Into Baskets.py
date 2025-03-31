# Problem link - https://leetcode.com/problems/fruit-into-baskets/
# Solution - https://www.youtube.com/watch?v=e3bs0uA1NhQ&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=5


class Solution:
    @staticmethod
    def fruits_in_basket(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(arr)

        # initialize a dictionary to maintain a reference to all the baskets.
        baskets = {}

        # initialize window pointers
        left, right = 0, 0

        # initialize the count of maximum fruits collected.
        fruits = 0

        # maintain the start index to return the window.
        start_index = 0

        # while there is ground to cover.
        while right < n:
            # increment the count of `right` indexed fruit by putting it into its basket.
            if arr[right] not in baskets:
                baskets[arr[right]] = 1
            else:
                baskets[arr[right]] += 1

            # after adding this fruit, if the number of baskets get more than 2, then it is not a valid case. We must
            # remove some fruits from the left side.
            if len(baskets) >= 3:
                baskets[arr[left]] -= 1
                # delete the basket if the `left` fruit count has become 0. This is done to quickly find the number of
                # baskets still in use in the next iteration. Otherwise, we would need to filter non-zero baskets.
                if baskets[arr[left]] == 0:
                    del baskets[arr[left]]
                # increment left pointer
                left += 1
            else:
                # if the number of baskets used <= 2, update the max count of fruits and update the start index.
                fruits = max(fruits, right - left + 1)
                start_index = left
            # finally, increment the right pointer as you've added the fruit pointed by `right` index into the basket
            # above.
            right += 1

        # return the max fruits count and the window of that as result.
        return fruits, arr[start_index:start_index + fruits]


print(Solution.fruits_in_basket([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_in_basket([1, 2, 1]))
print(Solution.fruits_in_basket([0, 1, 2, 2]))
print(Solution.fruits_in_basket([1, 2, 3, 2, 2]))
print(Solution.fruits_in_basket([3, 1, 2, 2, 2, 2]))
