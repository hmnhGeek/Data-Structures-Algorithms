class Solution:
    @staticmethod
    def _is_possible(arr, mid, m, k):
        bouquets_formed = 0
        flowers_used = 0
        for i in range(len(arr)):
            if mid >= arr[i]:
                flowers_used += 1
            else:
                flowers_used = 0
            if flowers_used == k:
                bouquets_formed += 1
                flowers_used = 0
        return bouquets_formed >= m

    @staticmethod
    def min_days_to_make_bouquets(arr, m, k):
        if m * k > len(arr):
            return -1
        low = min(arr)
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low) / 2)
            bouquets_possible = Solution._is_possible(arr, mid, m, k)
            if bouquets_possible:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.min_days_to_make_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_to_make_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_to_make_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_to_make_bouquets([1, 10, 3, 10, 2], 3, 1))
print(Solution.min_days_to_make_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_to_make_bouquets([5, 5, 5, 12, 10, 5, 5], 2, 3))
print(Solution.min_days_to_make_bouquets([7, 7, 3, 7, 7, 7], 1, 4))
