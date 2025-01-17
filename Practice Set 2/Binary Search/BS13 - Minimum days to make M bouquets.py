class Solution:
    @staticmethod
    def _find_num_formed(arr, mid, k):
        bouquets_formed = 0
        flowers_used = 0
        for i in range(len(arr)):
            if arr[i] <= mid:
                if flowers_used < k:
                    flowers_used += 1
                elif flowers_used == k:
                    bouquets_formed += 1
                    flowers_used = 1
            else:
                if flowers_used == k:
                    bouquets_formed += 1
                flowers_used = 0
        if flowers_used == k:
            bouquets_formed += 1
            flowers_used = 0
        return bouquets_formed

    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        n = len(arr)
        if m*k > n:
            return -1
        low, high = min(arr), max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            bouquets_formed = Solution._find_num_formed(arr, mid, k)
            if bouquets_formed < m:
                low = mid + 1
            else:
                high = mid - 1
        return low


print(Solution.min_days_for_m_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_for_m_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_for_m_bouquets([3, 4, 2, 7, 13, 8, 5], 3, 2))
print(Solution.min_days_for_m_bouquets([5, 5, 5, 5, 10, 5, 5], 2, 3))
