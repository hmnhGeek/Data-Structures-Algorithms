class Solution:
    @staticmethod
    def _less_than_equal_to_count(arr, k):
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
        return Solution._less_than_equal_to_count(arr, k) - Solution._less_than_equal_to_count(arr, k - 1)


print(Solution.get_subarray_count([1, 2, 1, 3, 4], 3))