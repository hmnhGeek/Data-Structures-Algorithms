class Solution:
    @staticmethod
    def get_single_element(arr):
        n = len(arr)
        if n == 0:
            return
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[-2] != arr[-1]:
            return arr[-1]
        low = 1
        high = n - 2
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
                return arr[mid]
            if (arr[mid] == arr[mid - 1] and mid % 2 == 1) or (arr[mid] == arr[mid + 1] and mid % 2 == 0):
                low = mid + 1
            else:
                high = mid - 1
        return None


print(Solution.get_single_element([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
print(Solution.get_single_element([1, 1, 2]))
print(Solution.get_single_element([1, 2, 2]))
print(Solution.get_single_element([1, 1, 2, 2, 4, 5, 5]))
print(Solution.get_single_element([1, 1, 3, 5, 5]))
print(Solution.get_single_element([1, 1, 4, 4, 15]))