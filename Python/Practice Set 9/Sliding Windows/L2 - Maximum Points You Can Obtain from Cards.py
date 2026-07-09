# Problem link - https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/0
# Solution - https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2


class Solution:
    @staticmethod
    def get_max_points(arr, k):
        """
            Time complexity is O(k) and space complexity is O(1).
        """
        if k <= 0:
            return
        i, j = k - 1, len(arr)
        max_sum = _sum = sum(arr[:k])
        while i >= 0:
            _sum -= arr[i]
            i -= 1
            j -= 1
            _sum += arr[j]
            max_sum = max(max_sum, _sum)
        return max_sum


print(Solution.get_max_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.get_max_points([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.get_max_points([2, 2, 2], 2))
print(Solution.get_max_points([8, 6, 2, 4, 5], 5))
