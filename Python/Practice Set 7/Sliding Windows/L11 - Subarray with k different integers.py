class Solution:
    @staticmethod
    def get_less_than_equal_to(arr, k):
        if k < 0:
            return 0
        n = len(arr)
        left = right = 0
        count = 0
        d = {i: 0 for i in arr}

        while right < n:
            d[arr[right]] += 1
            while Solution._get_distinct_count(d) > k:
                d[arr[left]] -= 1
                left += 1
            count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def _get_distinct_count(d):
        count = 0
        for i in d:
            if d[i] > 0:
                count += 1
        return count

    @staticmethod
    def get_subarray_count(arr, k):
        return Solution.get_less_than_equal_to(arr, k) - Solution.get_less_than_equal_to(arr, k - 1)


print(Solution.get_subarray_count([1, 2, 1, 3, 4], 3))
print(Solution.get_subarray_count([1, 2, 1, 2, 3], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 1))
print(Solution.get_subarray_count([2, 1, 3, 2, 4], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 4))
