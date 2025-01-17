# Problem link - https://www.naukri.com/code360/problems/rose-garden_2248080
# Solution - https://www.youtube.com/watch?v=TXAuxeYBTdg&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=14


class Solution:
    @staticmethod
    def _find_num_formed(arr, mid, k):
        bouquets_formed = 0
        flowers_used = 0
        for i in range(len(arr)):
            # if ith flower can bloom before or at midday
            if arr[i] <= mid:
                # if flowers used is < k, add this flower
                if flowers_used < k:
                    flowers_used += 1
                # if the flowers are already enough for making a bouquet
                elif flowers_used == k:
                    bouquets_formed += 1
                    # reset the flowers used to this flower as this was never used
                    flowers_used = 1
            else:
                # else, check if k flowers have already been used. If yes, increase bouquet count.
                if flowers_used == k:
                    bouquets_formed += 1
                flowers_used = 0

        # at the end, if k flowers have been used, do the same as `else`.
        if flowers_used == k:
            bouquets_formed += 1
            flowers_used = 0

        # return the count of bouquets formed.
        return bouquets_formed

    @staticmethod
    def min_days_for_m_bouquets(arr, m, k):
        """
            Time complexity is O(n * log(max - min)) and space complexity is O(1).
        """

        n = len(arr)
        # if the required number of flowers is more than n, return -1.
        if m*k > n:
            return -1

        # we must wait at least min(arr) number of days and at max(arr) day, all flowers will bloom.
        low, high = min(arr), max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)

            # find the number of bouquets that can be formed on midday.
            bouquets_formed = Solution._find_num_formed(arr, mid, k)

            # if the bouquets formed is less than required, we must wait more.
            if bouquets_formed < m:
                low = mid + 1
            else:
                # else we can decrease the day.
                high = mid - 1
        return low


print(Solution.min_days_for_m_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_for_m_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_for_m_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_for_m_bouquets([3, 4, 2, 7, 13, 8, 5], 3, 2))
print(Solution.min_days_for_m_bouquets([5, 5, 5, 5, 10, 5, 5], 2, 3))
