# Problem link - https://www.geeksforgeeks.org/k-th-missing-element-in-sorted-array/
# Solution - https://www.youtube.com/watch?v=uZ0N_hZpyps&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


class Solution:
    @staticmethod
    def get_kth_missing(arr, k):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # edge case
        if k <= 0:
            return -1

        # define a search space.
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)

            # number of missing integers
            num_missing = arr[mid] - mid - 1

            # if missing < k, we must move to right to accommodate more missing numbers.
            if num_missing < k:
                low = mid + 1

            # else we must move left
            elif num_missing == k:
                high = mid - 1
            else:
                high = mid - 1

        # return k + low, which points to the kth missing number.
        return k + low


print(Solution.get_kth_missing([2, 3, 4, 7, 11], 3))
print(Solution.get_kth_missing([2, 4, 5, 7], 3))
print(Solution.get_kth_missing([4, 7, 9, 10], 1))
print(Solution.get_kth_missing([4, 7, 9, 10], 4))
print(Solution.get_kth_missing([2, 3, 4, 7, 11], 5))
print(Solution.get_kth_missing([1, 2, 3, 4], 2))
print(Solution.get_kth_missing([3, 5, 9, 10, 11, 12], 2))
print(Solution.get_kth_missing([1, 2, 3], 2))
print(Solution.get_kth_missing([1, 2, 3], 0))
