class Solution:
    @staticmethod
    def search_in_rotated_sorted_array(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == x:
                return mid
            if arr[mid] <= arr[high]:
                if arr[mid] <= x <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif arr[low] <= x <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


arr1 = [7, 8, 9, 1, 2, 3, 4, 5, 6]
for i in arr1:
    print(Solution.search_in_rotated_sorted_array(arr1, i))
print(Solution.search_in_rotated_sorted_array(arr1, 100))