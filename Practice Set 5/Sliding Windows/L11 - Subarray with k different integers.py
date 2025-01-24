class Solution:
    @staticmethod
    def _count_less_than_equal_to(arr, k):
        if k < 0:
            return 0
        left = right = 0
        n = len(arr)
        d = {i: 0 for i in arr}
        count = 0
        while right < n:
            d[arr[right]] += 1
            while sum(1 for v in d.values() if v > 0) > k:
                d[arr[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v > 0) <= k:
                count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def get_subarray_count(arr, k):
        return Solution._count_less_than_equal_to(arr, k) - Solution._count_less_than_equal_to(arr, k - 1)


print(Solution.get_subarray_count([2, 1, 1, 1, 3, 4, 3, 2], 3))
print(Solution.get_subarray_count([1, 2, 1, 2, 3], 2))
print(Solution.get_subarray_count([1, 2, 1, 3, 4], 3))
print(Solution.get_subarray_count([2, 1, 2, 1, 6], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 1))
print(Solution.get_subarray_count([2, 1, 3, 2, 4], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 4))
