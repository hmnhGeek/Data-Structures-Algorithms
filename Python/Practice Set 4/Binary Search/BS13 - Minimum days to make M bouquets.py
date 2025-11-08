class Solution:
    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        n = len(arr)
        if m * k > n:
            return -1
        low, high = 0, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._is_possible(arr, mid, m, k)
            if is_possible:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def _is_possible(arr, mid, m, k):
        bouquets = 0
        flowers = 0
        for i in arr:
            if i <= mid:
                flowers += 1
            else:
                if flowers < k:
                    flowers = 0
                    continue
            if flowers == k:
                bouquets += 1
                flowers = 0
        return bouquets >= m


print(Solution.min_days_for_m_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_for_m_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_for_m_bouquets([3, 4, 2, 7, 13, 8, 5], 3, 2))
print(Solution.min_days_for_m_bouquets([5, 5, 5, 5, 10, 5, 5], 2, 3))
