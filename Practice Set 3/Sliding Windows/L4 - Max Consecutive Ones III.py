class Solution:
    @staticmethod
    def max_consecutive_1s(arr, k):
        left = right = 0
        n = len(arr)
        longest_length = 0
        start_index = -1
        used_zeros = 0
        while right < n:
            if arr[right] == 0:
                used_zeros += 1
            if used_zeros > k:
                if arr[left] == 0:
                    used_zeros -= 1
                left += 1
            if used_zeros <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index + longest_length] if start_index != -1 else []


print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_1s([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.max_consecutive_1s([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
