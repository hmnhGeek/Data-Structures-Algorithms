class Solution:
    @staticmethod
    def single_element(arr):
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[-1] != arr[-2]:
            return arr[-1]
        low, high = 2, len(arr) - 3
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]:
                return arr[mid]
            if arr[mid - 1] == arr[mid]:
                if (mid - low + 1 - 2) % 2 == 0:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (high - mid + 1 - 2) % 2 == 0:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


print(Solution.single_element([3, 3, 7, 7, 10, 11, 11]))
print(Solution.single_element([1, 1, 2, 2, 4, 5, 5]))
print(Solution.single_element([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
print(Solution.single_element([1, 1, 4, 4, 15]))
print(Solution.single_element([1, 1, 3, 5, 5]))
print(Solution.single_element([1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]))
print(Solution.single_element([1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]))
