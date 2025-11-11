def recursive():
    def count_subsets(arr, k):
        """
            Time complexity is exponential and space complexity is O(n).
        """
        n = len(arr)
        return solve(arr, n - 1, k)

    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        left = 0
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    print(count_subsets([1, 2, 2, 3], 3))
    print(count_subsets([1, 1, 4, 5], 5))
    print(count_subsets([1, 1, 1], 2))
    print(count_subsets([2, 34, 5], 40))
    print(count_subsets([1, 2, 3, 3], 6))
    print(count_subsets([1, 1, 1, 1], 1))
    print(count_subsets([5, 2, 3, 10, 6, 8], 10))
    print(count_subsets([2, 5, 1, 4, 3], 10))
    print(count_subsets([5, 7, 8], 3))
    print(count_subsets([35, 2, 8, 22], 0))


recursive()
print()
