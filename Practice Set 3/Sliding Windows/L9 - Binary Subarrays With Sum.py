class Solution:
    @staticmethod
    def _helper(arr, k):
        if k < 0:
            return 0
        left = right = 0
        n = len(arr)
        _sum = count = 0
        while right < n:
            _sum += arr[right]
            while _sum > k:
                _sum -= arr[left]
                left += 1
            if _sum <= k:
                count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def solve(arr, k):
        return Solution._helper(arr, k) - Solution._helper(arr, k - 1)


print(Solution.solve([1, 0, 1, 0, 1], 2))
print(Solution.solve([0, 0, 0, 0, 0], 0))
print(Solution.solve([1, 0, 1, 1, 0, 1], 2))
print(Solution.solve([1, 1, 0, 1, 1], 5))
print(Solution.solve([1, 0, 1, 1, 1, 0, 1], 3))
