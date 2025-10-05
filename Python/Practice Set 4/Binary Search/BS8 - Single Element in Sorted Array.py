# Problem link - https://www.naukri.com/code360/problems/unique-element-in-sorted-array_1112654
# Solution - https://www.youtube.com/watch?v=AZOmHuHadxQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=9


class Solution:
    @staticmethod
    def get_single_element(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        n = len(arr)
        if n == 0:
            return
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[-2] != arr[-1]:
            return arr[-1]
        low, high = 1, n - 2
        while low <= high:
            mid = int(low + (high - low)/2)

            if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
                return arr[mid]

            if (
                mid % 2 == 0 and arr[mid + 1] == arr[mid]
            ) or (
                mid % 2 == 1 and arr[mid - 1] == arr[mid]
            ):
                low = mid + 1
            else:
                high = mid - 1
        return -1


print(Solution.get_single_element([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
print(Solution.get_single_element([1, 1, 2]))
print(Solution.get_single_element([1, 2, 2]))
print(Solution.get_single_element([1, 1, 2, 2, 4, 5, 5]))
print(Solution.get_single_element([1, 1, 3, 5, 5]))
print(Solution.get_single_element([1, 1, 4, 4, 15]))
