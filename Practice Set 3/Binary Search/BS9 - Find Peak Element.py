# Problem link - https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
# Solution - https://www.youtube.com/watch?v=cXxmbemS6XM&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=10


class Solution:
    @staticmethod
    def get_peak(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        n = len(arr)
        if n == 1:
            return arr[0]
        if arr[0] > arr[1]:
            return arr[0]
        if arr[n - 1] > arr[n - 2]:
            return arr[n - 1]
        low, high = 1, n - 2
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


print(Solution.get_peak([1, 5, 1, 2, 1]))
print(Solution.get_peak([1, 8, 1, 5, 3]))
print(Solution.get_peak([1, 2, 1]))
print(Solution.get_peak([1, 2, 3, 1]))
print(Solution.get_peak([1, 2, 1, 3, 5, 6, 4]))
print(Solution.get_peak([1, 2, 4, 5, 7, 8, 3]))
print(Solution.get_peak([10, 20, 15, 2, 23, 90, 80]))
print(Solution.get_peak([1, 2, 3]))
