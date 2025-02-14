class Solution:
    @staticmethod
    def search(arr, x):
        # define the search space.
        low, high = 0, len(arr) - 1

        # binary search...
        while low <= high:
            mid = int(low + (high - low)/2)

            # if mid element is x, return mid.
            if arr[mid] == x:
                return mid

            # if left part is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= x <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # if right part is sorted and x could be in right part
            elif arr[mid] <= x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

        # if the element is not found, return -1.
        return -1


arr1 = [7, 8, 9, 1, 2, 3, 4, 5, 6]
for i in arr1:
    print(Solution.search(arr1, i))
print(Solution.search(arr1, 100))
print(Solution.search([12, 15, 18, 2, 4], 2))
print(Solution.search([8, 9, 4, 5], 3))
print(Solution.search([2, 3, 5, 8], 3))
print(Solution.search([1, 2, 3, 4], 4))
