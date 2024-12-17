# Problem link - https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
# Solution - https://www.youtube.com/watch?v=cXxmbemS6XM&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=10


class Solution:
    @staticmethod
    def get_peak(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # if there are no elements, return no peak
        if len(arr) == 0:
            return -1

        # if there's only one element, return it as peak
        if len(arr) == 1:
            return arr[0]

        # if 0th element is greater than 1st, return 0th element as peak
        if arr[0] > arr[1]:
            return arr[0]

        # if last element is greater than second last, return last element as peak
        if arr[-1] > arr[-2]:
            return arr[-1]

        # define a search space from 1 to n - 2
        low, high = 1, len(arr) - 2

        # typical Binary Search
        while low <= high:
            mid = int(low + (high - low) / 2)

            # if mid-element is a peak, return mid-element.
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]

            # if there is an increasing line to the right side, peak must lie on the right side.
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                low = mid + 1

            # if there is a downward slope, peak must lie on the left side.
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                high = mid - 1

            # else, if mid-element is a local minima, the peak can be on both sides, here, we move to the right side.
            else:
                low = mid + 1

        # if no peak is found, return -1.
        return -1


print(Solution.get_peak([1, 5, 1, 2, 1]))
print(Solution.get_peak([1, 8, 1, 5, 3]))
print(Solution.get_peak([1, 2, 1]))
print(Solution.get_peak([1, 2, 3, 1]))
print(Solution.get_peak([1, 2, 1, 3, 5, 6, 4]))
print(Solution.get_peak([1, 2, 4, 5, 7, 8, 3]))
print(Solution.get_peak([10, 20, 15, 2, 23, 90, 80]))
print(Solution.get_peak([1, 2, 3]))
