# Problem link - https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/


"""The idea is to start comparing from the leftmost element and find the difference between the current array element
and x. Let this difference be ‘diff’. From the given property of the array, we always know that x must be at least
‘diff/k’ away, so instead of searching one by one, we jump ‘diff/k’."""


class Solution:
    @staticmethod
    def search(arr, k, x):
        """
            This function takes O(n) time and O(1) space.
        """
        i = 0
        while i < len(arr):
            if arr[i] == x:
                return i
            i = i + max(1, abs(arr[i] - x)//k)
        return None


print(Solution.search([4, 5, 6, 7, 6], 1, 6))
print(Solution.search([20, 40, 50, 70, 70, 60], 20, 60))