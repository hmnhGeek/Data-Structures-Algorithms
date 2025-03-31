# Problem link - https://www.naukri.com/code360/problems/search-in-a-rotated-sorted-array-ii_7449547
# Solution - https://www.youtube.com/watch?v=w2G2W8l__pc&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=6


class Solution:
    @staticmethod
    def search(arr, x):
        """
            T: O_worst(n) and O_avg(log(n)) and S: O(1).
        """

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == x:
                return mid

            # if all three are same, then shrink the search space.
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
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


print(Solution.search([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 3))
print(Solution.search([3, 4, 5, 0, 0, 1, 2], 4))
print(Solution.search([31, 44, 56, 0, 10, 13], 47))
print(Solution.search([3, 3, 3, 1, 3, 3], 1))
print(Solution.search([3, 3, 3, 1, 3, 3], 3))
print(Solution.search([3, 1, 2, 3, 3, 3, 3], 1))