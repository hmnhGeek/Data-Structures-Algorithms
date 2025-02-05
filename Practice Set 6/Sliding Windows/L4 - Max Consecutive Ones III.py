class Solution:
    @staticmethod
    def max_consecutive_1s(arr, k):
        if k < 0:
            return []
        left = right = 0
        n = len(arr)
        zero_count = 0
        longest_length = 0
        start_index = -1
        while right < n:
            if arr[right] == 0:
                zero_count += 1
            if zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            if zero_count <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index+longest_length] if start_index != -1 else []


print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_1s([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.max_consecutive_1s([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
