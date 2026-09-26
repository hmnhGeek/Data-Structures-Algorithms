class Solution:
    @staticmethod
    def get_subarray_count(arr, k = 0):
        mp = {0: 1}
        _sum = count = 0
        for i in range(len(arr)):
            _sum += arr[i]
            if _sum - k in mp:
                count += mp[_sum - k]
            if _sum in mp:
                mp[_sum] += 1
            else:
                mp[_sum] = 1
        return count


print(Solution.get_subarray_count([6, -1, -3, 4, -2, 2, 4, 6, -12, -7]))  # Output: 4
print(Solution.get_subarray_count([0, 0, 5, 5, 0, 0]))  # Output: 6
print(Solution.get_subarray_count([0]))  # Output: 1
print(Solution.get_subarray_count([1, 2, -3, 3, -1, -1]))  # Output: 3
print(Solution.get_subarray_count([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3)) # Output: 8