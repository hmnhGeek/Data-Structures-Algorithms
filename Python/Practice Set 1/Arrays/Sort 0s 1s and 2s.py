# Problem link - https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1


class Solution:
    @staticmethod
    def dnf_sort(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        """
            The idea is that all elements from 0 to low - 1 will be 0s.
            All elements from mid to high - 1 will be 1s.
            All elements from high till end will be 2s.
        """
        n = len(arr)
        low, mid, high = 0, 0, n - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1


# Example 1
a1 = [0, 1, 2, 0, 1, 2]
Solution.dnf_sort(a1)
print(a1)

# Example 2
a2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Solution.dnf_sort(a2)
print(a2)