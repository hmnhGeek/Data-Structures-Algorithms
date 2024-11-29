def recursive():
    def solve(arr, i, j):
        if j == 0:
            return False
        if i == 0:
            return arr[0] == j

        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([1, 2, 3, 4], 9))
    print(subset_sum([1, 2, 3, 4], 5))


recursive()