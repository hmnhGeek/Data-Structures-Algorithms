class Solution:
    @staticmethod
    def get_max_consecutive_ones(arr, k):
        left = right = 0
        n = len(arr)
        zero_count = 0
        max_length = 0
        start_index = -1
        while right < n:
            if arr[right] == 0:
                zero_count += 1
            if zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            if zero_count <= k:
                max_length = max(max_length, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index+max_length] if start_index != -1 else []


print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.get_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.get_max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))