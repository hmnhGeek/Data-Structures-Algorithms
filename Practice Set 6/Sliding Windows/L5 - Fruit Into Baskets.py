class Solution:
    @staticmethod
    def fruits_into_baskets(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking variables.
        d = {i: 0 for i in arr}

        # define result variables
        count = 0
        start_index = -1

        # while there is ground to cover
        while right < n:
            # increment right index count
            d[arr[right]] += 1

            # if more than 2 baskets have been used, shrink one unit from left.
            if sum(1 for v in d.values() if v > 0) > 2:
                d[arr[left]] -= 1
                left += 1

            # if baskets are under control, update the result variables.
            if sum(1 for v in d.values() if v > 0) <= 2:
                count = max(count, right - left + 1)
                start_index = left

            # increment right index
            right += 1

        # return the subarray
        return arr[start_index:start_index+count] if start_index != -1 else []


print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([1, 1, 2, 3]))
print(Solution.fruits_into_baskets([1, 2, 3, 4]))
