# Problem link - https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1
# Solution - https://www.youtube.com/watch?v=TXAuxeYBTdg&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=14


class Solution:
    @staticmethod
    def _is_possible(arr, mid, m, k):
        # store the count of bouquets formed and the flowers used.
        bouquets_formed = 0
        flowers_used = 0

        # loop on the flowers with `mid` day as the count of bloom days.
        for i in range(len(arr)):
            # if ith flower requires less than or equal to mid days to bloom, we can use this flower
            if mid >= arr[i]:
                flowers_used += 1
            else:
                # else there is a discontinuity, set the flowers count back to 0.
                flowers_used = 0

            # if the required number of adjacent flowers have been used...
            if flowers_used == k:
                # increase the count of bouquets
                bouquets_formed += 1
                # reset the flowers used
                flowers_used = 0

        # return if more than or equal to m bouquets were formed or not.
        return bouquets_formed >= m

    @staticmethod
    def min_days_to_make_bouquets(arr, m, k):
        """
            Overall time complexity is O(n * log(max - min)) and space complexity is O(1).
        """

        # if the required number of flowers is more than the length of the array, then bouquet formation is not
        # possible. In this case, return -1.
        if m * k > len(arr):
            return -1

        # define search space for the binary search
        low = min(arr)
        high = max(arr)

        while low <= high:
            mid = int(low + (high - low) / 2)

            # if `m` bouquets can be formed by taking `k` adjacent bloomed flowers.
            bouquets_possible = Solution._is_possible(arr, mid, m, k)

            # if it is possible, then we may try to reduce the number of days to see if some lower day count can
            # achieve the same result or not.
            if bouquets_possible:
                high = mid - 1
            else:
                # else if blooming was not possible, we must increase blooming day count.
                low = mid + 1

        # return `low` which points to the number of days required to make such bouquets.
        return low


print(Solution.min_days_to_make_bouquets([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(Solution.min_days_to_make_bouquets([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(Solution.min_days_to_make_bouquets([1, 1, 1, 1], 1, 1))
print(Solution.min_days_to_make_bouquets([1, 10, 3, 10, 2], 3, 1))
print(Solution.min_days_to_make_bouquets([1, 10, 3, 10, 2], 3, 2))
print(Solution.min_days_to_make_bouquets([5, 5, 5, 12, 10, 5, 5], 2, 3))
print(Solution.min_days_to_make_bouquets([7, 7, 3, 7, 7, 7], 1, 4))
