class Solution:
    @staticmethod
    def subarray_with_0_sum(arr):
        d = {0: -1}
        _sum = 0
        max_length = 0
        start_index = -1
        for i in range(len(arr)):
            _sum += arr[i]
            if _sum in d:
                start_index = d[_sum] + 1
                max_length = i - d[_sum]
            else:
                d[_sum] = i
        return arr[start_index:start_index+max_length] if start_index != -1 else []


print(Solution.subarray_with_0_sum([4, 2, -3, 1, 6]))
print(Solution.subarray_with_0_sum([9, -3, 3, -1, 6, -5]))
print(Solution.subarray_with_0_sum([4, 2, 0, 1, 6]))
print(Solution.subarray_with_0_sum([1, 4, -5]))