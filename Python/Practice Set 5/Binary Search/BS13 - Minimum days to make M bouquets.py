# Problem link - https://www.naukri.com/code360/problems/rose-garden_2248080
# Solution - https://www.youtube.com/watch?v=TXAuxeYBTdg&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=14


class Solution:
    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        """
            Time complexity is O(n * log(max(arr))) and space complexity is O(1).
        """
        if m * k > len(arr):
            return -1
        low, high = min(arr), max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            bouquets_formed = Solution._get_formed_bouquets(arr, mid, k)
            if bouquets_formed < m:
                low = mid + 1
            elif bouquets_formed == m:
                high = mid - 1
            else:
                high = mid - 1
        return low

    @staticmethod
    def _get_formed_bouquets(arr, mid, k):
        bouquets_formed = 0
        adjacent_flowers_count = 0
        for i in range(len(arr)):
            bloom_threshold = arr[i]
            if bloom_threshold <= mid:
                adjacent_flowers_count += 1
            else:
                adjacent_flowers_count = 0
            if adjacent_flowers_count == k:
                bouquets_formed += 1
                adjacent_flowers_count = 0
        return bouquets_formed


print(Solution.min_days_for_m_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_for_m_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_for_m_bouquets([3, 4, 2, 7, 13, 8, 5], 3, 2))
print(Solution.min_days_for_m_bouquets([5, 5, 5, 5, 10, 5, 5], 2, 3))
