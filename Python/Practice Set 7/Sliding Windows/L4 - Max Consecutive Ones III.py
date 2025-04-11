class Solution:
    @staticmethod
    def get_max_consecutive_ones(arr, k):
        if k < 0:
            return -1
        n = len(arr)
        left = right = 0
        start_index = -1
        longest_length = 0
        count_of_zeros = 0
        while right < n:
            if arr[right] == 0:
                count_of_zeros += 1
            if count_of_zeros > k:
                if arr[left] == 0:
                    count_of_zeros -= 1
                left += 1
            if count_of_zeros <= k:
                start_index = left
                longest_length = max(right - left + 1, longest_length)
            right += 1
        return arr[start_index:start_index+longest_length] if start_index != -1 else []


print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.get_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.get_max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))

