# Problem link - https://www.naukri.com/code360/problems/rose-garden_2248080
# Solution - https://www.youtube.com/watch?v=TXAuxeYBTdg&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=14


class Solution:
    @staticmethod
    def _find_formed_bouquets_count(arr, mid, k):
        bouquets = 0
        flowers_used = 0
        n = len(arr)

        for i in range(n):
            # if at ith-day, the blooming threshold is more than mid, then set flowers used as 0 and continue for the
            # next day, as we have found a discontinuity.
            if arr[i] > mid:
                flowers_used = 0
                continue

            # else, increment the flower count.
            flowers_used += 1

            # if flower count matches k, increment bouquets and reset flower count.
            if flowers_used == k:
                bouquets += 1
                flowers_used = 0

        # return the count of bouquets formed.
        return bouquets

    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        """
            Time complexity is O(n * log(max(arr))) and space complexity is O(1).
        """

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
