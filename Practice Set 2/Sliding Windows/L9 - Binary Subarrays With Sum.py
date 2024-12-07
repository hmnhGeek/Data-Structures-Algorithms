class Solution:
    @staticmethod
    def _get_count(arr, goal):
        if goal < 0:
            return 0
        left = right = 0
        n = len(arr)
        _sum = 0
        count = 0
        while right < n:
            _sum += arr[right]
            while _sum > goal:
                _sum -= arr[left]
                left += 1
            count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def get_count(arr, goal):
        return Solution._get_count(arr, goal) - Solution._get_count(arr, goal - 1)


print(Solution.get_count([1, 0, 1, 0, 1], 2))
print(Solution.get_count([0, 0, 0, 0, 0], 0))
print(Solution.get_count([1, 0, 1, 1, 0, 1], 2))
print(Solution.get_count([1, 0, 1, 1, 1, 0, 1], 3))
print(Solution.get_count([1, 1, 0, 1, 1], 5))
