# Problem link - https://www.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1
# Solution - https://www.youtube.com/watch?v=0Hkh1cjnBNA


class Solution:
    @staticmethod
    def min_swaps(arr, k):
        n = len(arr)
        window_size = Solution._get_fixed_window_size(arr, k, n)
        non_favs = 0
        ans = 1e6
        for i in range(window_size):
            if arr[i] > k:
                non_favs += 1
        ans = min(ans, non_favs)
        end_index = window_size - 1
        while end_index < n - 1:
            start_index = end_index - window_size + 1
            if arr[start_index] > k:
                non_favs -= 1
            start_index += 1
            if arr[end_index + 1] > k:
                non_favs += 1
            end_index += 1
            ans = min(ans, non_favs)
        return ans

    @staticmethod
    def _get_fixed_window_size(arr, k, n):
        result = 0
        for i in range(n):
            if arr[i] <= k:
                result += 1
        return result


print(Solution.min_swaps([2, 1, 5, 6, 3], 3))
print(Solution.min_swaps([2, 7, 9, 5, 8, 7, 4], 6))
print(Solution.min_swaps([2, 4, 5, 3, 6, 1, 8], 6))
