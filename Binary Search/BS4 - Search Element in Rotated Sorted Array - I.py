class Solution:
    @staticmethod
    def search_in_rotated_sorted(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == x:
                return mid
            if arr[mid] < arr[high]:
                if arr[mid] < x <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if arr[low] <= x < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


def test(arr):
    for i in arr:
        print(f"{i} found at index = {Solution.search_in_rotated_sorted(arr, i)}")
    print(f"{100} found at index = {Solution.search_in_rotated_sorted(arr, 100)}")
    print()


test([7, 8, 9, 1, 2, 3, 4, 5, 6])
test([12, 15, 18, 2, 4])
test([8, 9, 4, 5])
test([2, 3, 5, 8])