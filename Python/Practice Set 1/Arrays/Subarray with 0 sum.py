# Problem link - https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
# Solution - https://www.youtube.com/watch?v=xvNwoz-ufXA


class Solution:
    @staticmethod
    def has_zero_sum(arr, k = 0):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        d = {0: 1}
        prefix_sum = count = i = 0
        n = len(arr)
        while i < n:
            prefix_sum += arr[i]
            if prefix_sum - k in d:
                count += d[prefix_sum - k]
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1
            i += 1
        return count


print(Solution.has_zero_sum([4, 2, -3, 1, 6]))
print(Solution.has_zero_sum([4, 2, 0, 1, 6]))
print(Solution.has_zero_sum([1, 2, -1]))
print(Solution.has_zero_sum([1, 1, 1], 2))
print(Solution.has_zero_sum([1, 2, 3], 3))