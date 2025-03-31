# Problem link - https://www.geeksforgeeks.org/number-subarrays-m-odd-numbers/
# Solution - https://www.youtube.com/watch?v=j_QOv9OT9Og&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=10


class Solution:
    """
        This problem is exactly same as L9.
        T: O(2n) and S: O(1).
    """

    @staticmethod
    def _count(arr, goal):
        if goal < 0:
            return 0
        left = right = 0
        n = len(arr)
        _sum = 0
        count = 0
        while right < n:
            _sum += (arr[right] % 2)
            while _sum > goal:
                _sum -= (arr[left] % 2)
                left += 1
            count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def get_count(arr, goal):
        return Solution._count(arr, goal) - Solution._count(arr, goal - 1)


print(Solution.get_count([1, 5, 1, 2, 1, 1], 3))
print(Solution.get_count([1, 1, 2, 1, 1], 2))
print(Solution.get_count([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.get_count([2, 4, 6], 1))
print(Solution.get_count([2, 5, 6, 9], 2))
print(Solution.get_count([2, 2, 5, 6, 9, 2, 11], 2))
