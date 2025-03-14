class Solution:
    @staticmethod
    def _find_formed_bouquets_count(arr, mid, k):
        bouquets = 0
        flowers_used = 0
        n = len(arr)
        for i in range(n):
            if arr[i] > mid:
                flowers_used = 0
                continue
            flowers_used += 1
            if flowers_used == k:
                bouquets += 1
                flowers_used = 0
        return bouquets

    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        # if more than length of arr flowers are needed, return -1.
        if m * k > len(arr):
            return -1

        # define a search space.
        low, high = 1, max(arr)

        # typical binary search.
        while low <= high:
            # get the mid-day.
            mid = int(low + (high - low)/2)

            # find the number of bouquets formed at mid-day.
            bouquets_formed = Solution._find_formed_bouquets_count(arr, mid, k)

            # if less than required bouquets are formed, increase the day.
            if bouquets_formed < m:
                low = mid + 1

            # else if >= required bouquets are formed, try searching for lower day.
            elif bouquets_formed == m:
                high = mid - 1
            else:
                high = mid - 1

        # return low, which points to the minimum day.
        return low


print(Solution.min_days_for_m_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_for_m_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_for_m_bouquets([3, 4, 2, 7, 13, 8, 5], 3, 2))
print(Solution.min_days_for_m_bouquets([5, 5, 5, 5, 10, 5, 5], 2, 3))
