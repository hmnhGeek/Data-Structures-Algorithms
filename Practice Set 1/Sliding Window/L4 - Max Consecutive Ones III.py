class Solution:
    @staticmethod
    def get_max_consecutive_ones(arr, k):
        if k < 0:
            return
        n = len(arr)
        longest_length = 0
        count = 0
        start_index = 0
        left, right = 0, 0
        while right < n:
            if arr[right] == 1:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
                right += 1
            else:
                if count < k:
                    count += 1
                    longest_length = max(longest_length, right - left + 1)
                    start_index = left
                    right += 1
                else:
                    if arr[left] == 0:
                        count -= 1
                    left += 1
        return longest_length, arr[start_index:start_index+longest_length]


print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.get_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.get_max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
