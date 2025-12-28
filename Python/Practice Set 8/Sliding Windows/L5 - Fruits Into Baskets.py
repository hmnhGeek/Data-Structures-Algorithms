# Problem link - https://www.naukri.com/code360/problems/distinct-characters_2221410
# Solution - https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6


class Solution:
    @staticmethod
    def fruits_into_baskets(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        n = len(arr)
        left = right = 0
        start_index = -1
        length = 0
        d = {i: 0 for i in arr}
        while right < n:
            d[arr[right]] += 1
            while sum(1 for i in d.values() if i > 0) > 2:
                d[arr[left]] -= 1
                left += 1
            if right - left + 1 > length:
                length = right - left + 1
                start_index = left
            right += 1
        if start_index != -1:
            return arr[start_index:start_index+length]
        return []


print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([1, 1, 2, 3]))
print(Solution.fruits_into_baskets([1, 2, 3, 4]))
