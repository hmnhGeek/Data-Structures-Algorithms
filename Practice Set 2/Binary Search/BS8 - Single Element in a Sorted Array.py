class Solution:
    @staticmethod
    def get_element(arr):
        n = len(arr)
        if n == 0:
            return None
        if n == 1:
            return arr[0]
        if n == 2 and arr[0] != arr[1]:
            return arr[0]
        if n == 3:
            if arr[0] != arr[1]:
                return arr[0]
            return arr[-1]
        low, high = 1, n - 2
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
                return arr[mid]
            if (mid % 2 == 1 and arr[mid - 1] == arr[mid]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
        return -1


print(Solution.get_element([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
print(Solution.get_element([1, 1, 2]))
print(Solution.get_element([1, 2, 2]))
