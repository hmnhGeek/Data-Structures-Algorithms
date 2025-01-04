# Problem link - https://www.spoj.com/problems/EKO/
# Solution - https://www.youtube.com/watch?v=tkoucfh10SI&t=863s


class Solution:
    @staticmethod
    def _collect_wood(arr, mid):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # store the collected wood
        collected = 0

        # loop on each tree
        for i in range(len(arr)):
            # if the ht of the tree is more than saw ht, we can collect the extra wood.
            if arr[i] > mid:
                collected += (arr[i] - mid)
        return collected

    @staticmethod
    def get_max_ht(arr, k):
        """
            Time complexity is O(n * log(max(arr))) and space complexity is O(1).
        """

        # if you require more than collective tree wood, or k <= 0, your requirement could not be fulfilled, return -1.
        if k > sum(arr) or k <= 0:
            return -1

        # define a search space for the binary search.
        n = len(arr)
        # at minimum, the saw can be at 0 ht and at maximum, it can be at the ht of max tree.
        low, high = 0, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            # let's find the amount of wood collected when saw is at ht of mid.
            wood_collected = Solution._collect_wood(arr, mid)

            # if the collected wood is same as required wood, maybe we can try to increase the ht of the saw to reduce
            # wood wastage
            if wood_collected == k:
                low = mid + 1

            # if the wood collected is less than required wood, we must decrease saw ht so that more wood can be
            # collected.
            elif wood_collected < k:
                high = mid - 1

            # if more than k wood was collected, we should increase ht of the saw as we don't need this extra wood.
            else:
                low = mid + 1

        # high points to the correct ht at which saw should be placed.
        return high


print(Solution.get_max_ht([20, 15, 10, 17], 7))
print(Solution.get_max_ht([4, 42, 40, 26, 46], 20))
