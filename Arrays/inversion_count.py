class Solution:
    @staticmethod
    def no_space(arr):
        """
            Total time complexity is O(n^2) and space complexity is O(1).
        """

        count = 0
        n = len(arr)
        # loop on the array
        for i in range(n):
            # take `j` from `i + 1` --> `n - 1`
            for j in range(i + 1, n):
                # if at any point, a_i > a_j, increment the inversion count.
                if arr[i] > arr[j]:
                    count += 1
        return count


print(Solution.no_space([2, 4, 1, 3, 5]))
print(Solution.no_space([2, 3, 4, 5, 6]))
print(Solution.no_space([10, 10, 10]))
print(Solution.no_space([4, 3, 2, 1]))
print(Solution.no_space([5, 4, 3, 2, 1]))
