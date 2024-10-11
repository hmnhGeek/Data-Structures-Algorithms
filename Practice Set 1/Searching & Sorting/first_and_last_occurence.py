# Problem link - https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1


class Solution:
    @staticmethod
    def get_first_and_last(arr, elem):
        """
            Overall time complexity is O(log(n)) and space complexity is O(1).
        """
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] >= elem:
                high = mid - 1
            else:
                low = mid + 1
        first_occ = low if arr[low] == elem else -1

        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] <= elem:
                low = mid + 1
            else:
                high = mid - 1
        last_occ = high if arr[high] == elem else -1
        return first_occ, last_occ


print(Solution.get_first_and_last([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))
print(Solution.get_first_and_last([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))
print(Solution.get_first_and_last([1, 3, 5, 5, 5, 5, 7, 123, 125], 90))
