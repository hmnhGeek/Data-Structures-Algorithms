class Solution:
    @staticmethod
    def max_consecutive_ones(arr, k):
        n = len(arr)
        left = right = 0
        longest_length = 0
        start_index = -1
        count_zeroes = 0
        while right < n:
            if arr[right] == 0:
                count_zeroes += 1
            if count_zeroes > k:
                if arr[left] == 0:
                    count_zeroes -= 1
                left += 1
            if count_zeroes <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index + longest_length] if start_index != -1 else []


print(Solution.max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
