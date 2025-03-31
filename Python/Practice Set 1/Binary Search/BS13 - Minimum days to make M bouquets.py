# Problem link - https://www.naukri.com/code360/problems/rose-garden_2248080
# Solution - https://www.youtube.com/watch?v=TXAuxeYBTdg&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=14


class Solution:
    @staticmethod
    def _is_possible(arr, mid, m, k):
        # track the adjacent flowers used and the number of bouquets formed.
        flowers_used = 0
        bouquets_formed = 0

        # loop on the flowers.
        for i in range(len(arr)):
            # if the ith flower takes <= mid number of days to bloom, add it to the used flowers count.
            if arr[i] <= mid:
                flowers_used += 1
            else:
                # if there's a discontinuity, reset the count of flowers used.
                flowers_used = 0

            # if flowers used == k, that means we can form a bouquet
            if flowers_used == k:
                bouquets_formed += 1
                # reset the flowers used.
                flowers_used = 0

        # return True if m bouquets can be formed, else False.
        return bouquets_formed >= m

    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        """
            Time complexity is O(n * log(max - min)) and space complexity is O(1).
        """

        n = len(arr)
        # if the requirement demands more number of flowers than we have, return -1.
        if m * k > n:
            return -1

        # define a search space. Minimum, we need to wait for min number of days and max when all the flowers have
        # bloomed.
        low, high = min(arr), max(arr)
        while low <= high:
            mid = int(low + (high - low) / 2)
            # if we take mid-number of days, check if it is possible to make m bouquets with k adjacent flowers.
            is_possible = Solution._is_possible(arr, mid, m, k)
            if is_possible:
                # if yes, then let's try to lower the number of days.
                high = mid - 1
            else:
                # else we must increase the number of days.
                low = mid + 1

        # return low which points to the minimum number of days we must wait for all k adjacent flowers to bloom so that
        # we can make m bouquets.
        return low


print(Solution.min_days_for_m_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_for_m_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_for_m_bouquets([3, 4, 2, 7, 13, 8, 5], 3, 2))
print(Solution.min_days_for_m_bouquets([5, 5, 5, 5, 10, 5, 5], 2, 3))
