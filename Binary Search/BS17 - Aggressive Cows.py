class Solution:
    @staticmethod
    def _placing_all_cows_possible(arr, mid, k):
        cows_placed = 1
        last_cow_index = 0
        for i in range(1, len(arr)):
            if arr[i] - arr[last_cow_index] >= mid:
                cows_placed += 1
                last_cow_index = i
        return cows_placed >= k

    @staticmethod
    def aggressive_cows(arr, k):
        if k <= 0:
            return
        arr.sort()
        low, high = 1, arr[-1] - arr[0]
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._placing_all_cows_possible(arr, mid, k)
            if is_possible:
                low = mid + 1
            else:
                high = mid - 1
        return high


print(Solution.aggressive_cows([0, 3, 4, 7, 9, 10], 4))
print(Solution.aggressive_cows([1, 2, 3], 2))
print(Solution.aggressive_cows([4, 2, 1, 3, 6], 2))
print(Solution.aggressive_cows([1, 2, 4, 8, 9], 3))
print(Solution.aggressive_cows([10, 1, 2, 7, 5], 3))