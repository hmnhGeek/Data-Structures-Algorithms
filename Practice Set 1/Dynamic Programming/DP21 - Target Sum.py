def recursive():
    def solve(arr, index, target):
        if target == 0:
            return 1

        if index == 0:
            return 1 if arr[0] == target else 0

        left = 0
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index])
        right = solve(arr, index - 1, target)
        return left + right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([2, 1, 3, 1], 5))
    print(subset_sum([1, 2, 3, 3], 6))
    print(subset_sum([1, 1, 1, 1], 1))


recursive()