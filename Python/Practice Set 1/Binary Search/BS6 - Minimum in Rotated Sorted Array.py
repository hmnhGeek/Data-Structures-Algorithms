# Problem link - https://www.naukri.com/code360/problems/rotated-array_1093219
# Solution - https://www.youtube.com/watch?v=nhEMDKMB44g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=7


class Solution:
    @staticmethod
    def _is_min(arr, mid, n):
        if mid == 0 and arr[0] <= arr[1]:
            return arr[0]
        if mid == n - 1 and arr[-2] >= arr[-1]:
            return arr[-1]
        return arr[mid - 1] >= arr[mid] and arr[mid + 1] >= arr[mid]

    @staticmethod
    def get_min(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            return arr[0]

        # define a search space.
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)

            # if mid-element is minimum, then it's the correct answer, return it.
            if Solution._is_min(arr, mid, len(arr)):
                return arr[mid]

            # if from low to high, we have a increasing sequence, then min will be in lower half.
            if arr[low] <= arr[high]:
                high = mid - 1
            # if lower half is sorted, then upper half must be unsorted and the min would be there.
            elif arr[low] <= arr[mid]:
                low = mid + 1
            else:
                # else the lower half is unsorted and min must be there.
                high = mid - 1

        # return the `low` index value denoting the min element in the array.
        return arr[low] if 0 <= low <= len(arr) - 1 else -1


print(Solution.get_min([4, 1, 2, 3]))
print(Solution.get_min([3, 4, 5, 1, 2]))
print(Solution.get_min([3, 4, 1, 2]))
print(Solution.get_min([25, 30, 5, 10, 15, 20]))
print(Solution.get_min([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_min([11, 13, 15, 17]))
print(Solution.get_min([4, 2, 3]))
print(Solution.get_min([7, 8, 1, 2, 3, 4, 5, 6]))
print(Solution.get_min([1, 2]))
print(Solution.get_min([2, 1]))
print(Solution.get_min([3, 3, 3, 3, 3]))
print(Solution.get_min([1, 2, 2, 3, 3, 3, 5]))
print(Solution.get_min([5, 5, 5, 5, 1, 2, 3, 3]))
