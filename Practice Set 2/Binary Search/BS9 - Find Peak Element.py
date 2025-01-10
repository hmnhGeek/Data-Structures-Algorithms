# Problem link - https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
# Solution - https://www.youtube.com/watch?v=cXxmbemS6XM&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=10


class Solution:
    @staticmethod
    def get_peak(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        n = len(arr)

        # if there is no element, return -inf as peak
        if n == 0:
            return -1e6

        # if there's only one element, return it as the peak
        if n == 1:
            return arr[0]

        # if 0th element is greater than 1st element, 0th element is the peak
        if arr[1] < arr[0]:
            return arr[0]

        # if last element is greater than second last element, then last element is the peak
        if arr[-1] > arr[-2]:
            return arr[-1]

        # define search space from 1 to n - 2 so that mid has left and right elements.
        low, high = 1, n - 2
        while low <= high:
            mid = int(low + (high - low)/2)

            # if mid is peak, return it
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return arr[mid]

            # if mid is on increasing slope, the peak is on right side
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                low = mid + 1

            # if mid is on decreasing slope, the peak is on left side
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                high = mid - 1

            # if mid is the local minima, move to any side to catch the peak
            else:
                low = mid + 1

        # return -1 if no peak is found
        return -1


print(Solution.get_peak([1, 5, 1, 2, 1]))
print(Solution.get_peak([1, 8, 1, 5, 3]))
print(Solution.get_peak([1, 2, 1]))
print(Solution.get_peak([1, 2, 3, 1]))
print(Solution.get_peak([1, 2, 1, 3, 5, 6, 4]))
print(Solution.get_peak([1, 2, 4, 5, 7, 8, 3]))
print(Solution.get_peak([10, 20, 15, 2, 23, 90, 80]))
print(Solution.get_peak([1, 2, 3]))
