class Solution:
    @staticmethod
    def _count_less_than_equal_to(arr, k):
        if k < 0:
            return 0
        left = right = 0
        n = len(arr)
        _sum = count = 0
        while right < n:
            _sum += arr[right] % 2
            while _sum > k:
                _sum -= arr[left] % 2
                left += 1
            if _sum <= k:
                count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def count_nice_subarrays(arr, k):
        return Solution._count_less_than_equal_to(arr, k) - Solution._count_less_than_equal_to(arr, k - 1)


print(Solution.count_nice_subarrays([1, 1, 2, 1, 1], 3))
print(Solution.count_nice_subarrays([2, 4, 6], 1))
print(Solution.count_nice_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.count_nice_subarrays([2, 5, 6, 9], 2))
print(Solution.count_nice_subarrays([2, 2, 5, 6, 9, 2, 11], 2))
