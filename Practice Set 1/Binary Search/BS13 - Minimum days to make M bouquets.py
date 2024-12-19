class Solution:
    @staticmethod
    def _is_possible(arr, mid, m, k):
        flowers_used = 0
        bouquets_formed = 0
        for i in range(len(arr)):
            if arr[i] <= mid:
                flowers_used += 1
            else:
                flowers_used = 0
            if flowers_used == k:
                bouquets_formed += 1
                flowers_used = 0
        return bouquets_formed >= m

    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        n = len(arr)
        if m * k > n:
            return -1
        low, high = min(arr), max(arr)
        while low <= high:
            mid = int(low + (high - low) / 2)
            is_possible = Solution._is_possible(arr, mid, m, k)
            if is_possible:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.min_days_for_m_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_for_m_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_for_m_bouquets([3, 4, 2, 7, 13, 8, 5], 3, 2))
print(Solution.min_days_for_m_bouquets([5, 5, 5, 5, 10, 5, 5], 2, 3))
