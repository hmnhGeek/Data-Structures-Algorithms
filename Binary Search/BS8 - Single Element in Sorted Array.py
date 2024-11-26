class Solution:
    @staticmethod
    def get_single_element(arr):
        n = len(arr)

        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        low = 0
        high = n - 1
        while low <= high:
            mid = int(low + (high - low)/2)

            if arr[mid - 1] != arr[mid] and arr[mid + 1] != arr[mid]:
                return arr[mid]

            if arr[mid - 1] == arr[mid]:
                left_count = mid - low - 1
            else:
                left_count = mid - low

            if arr[mid + 1] == arr[mid]:
                right_count = high - mid - 1
            else:
                right_count = high - mid

            if left_count % 2 == 1:
                high = mid - 1
            else:
                low = mid + 1
        return -1


print(Solution.get_single_element([1, 2, 2, 3, 3, 4, 4]))
print(Solution.get_single_element([1, 1, 2, 3, 3, 4, 4]))
print(Solution.get_single_element([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
print(Solution.get_single_element([1, 1, 2, 2, 3]))
print(Solution.get_single_element([1, 1, 2, 2, 4, 5, 5]))
print(Solution.get_single_element([1, 1, 3, 5, 5]))
print(Solution.get_single_element([1, 1, 4, 4, 15]))
