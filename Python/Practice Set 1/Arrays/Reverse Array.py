class Solution:
    @staticmethod
    def reverse(arr):
        n = len(arr)
        if n == 0 or n == 1:
            return arr
        i, j = 0, n - 1
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr


print(Solution.reverse([1, 2, 3, 4]))
print(Solution.reverse([1, 2, 3, 4, 5]))
print(Solution.reverse([1, 4, 3, 2, 6, 5]))
print(Solution.reverse([4, 5, 1, 2]))
