class Solution:
    @staticmethod
    def max_consecutive_ones(arr, k):
        if k <= 0:
            return

        left = right = 0
        n = len(arr)
        longest_length = 0
        start_index = -1
        counter = k
        while right < n:
            if arr[right] == 0:
                counter -= 1
            if counter < 0:
                if arr[left] == 0:
                    counter += 1
                left += 1
            else:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index + longest_length] if start_index != -1 else -1


print(Solution.max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
