class Solution:
    @staticmethod
    def get_min(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define a search space.
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)

            # if mid-element is minimum, then it's the correct answer, return it.
            if arr[low] >= arr[mid] and arr[high] >= arr[mid]:
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
