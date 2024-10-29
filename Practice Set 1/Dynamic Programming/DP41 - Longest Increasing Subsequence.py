def recursive():
    def solve(arr, index, prev):
        if index < 0:
            return 0

        left = 0
        if arr[index] < prev:
            left = 1 + solve(arr, index - 1, arr[index])
        right = solve(arr, index - 1, prev)
        return max(left, right)

    def longest_increasing_subsequence(arr):
        n = len(arr)
        return solve(arr, n - 1, 1e6)

    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
    print(longest_increasing_subsequence([1, 2, 2]))


recursive()