class Solution:
    @staticmethod
    def _get_count_less_than_equal_to(arr, k):
        if k < 0:
            return 0
        left = right = 0
        n = len(arr)
        count_odds = 0
        count = 0
        while right < n:
            count_odds += arr[right] % 2
            while count_odds > k:
                count_odds -= arr[left] % 2
                left += 1
            if count_odds <= k:
                count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def get_nice_subarray_count(arr, k):
        return Solution._get_count_less_than_equal_to(arr, k) - Solution._get_count_less_than_equal_to(arr, k - 1)


print(Solution.get_nice_subarray_count([1, 5, 2, 1, 1], 3))
print(Solution.get_nice_subarray_count([2, 4, 6], 1))
print(Solution.get_nice_subarray_count([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.get_nice_subarray_count([2, 5, 6, 9], 2))
print(Solution.get_nice_subarray_count([2, 2, 5, 6, 9, 2, 11], 2))