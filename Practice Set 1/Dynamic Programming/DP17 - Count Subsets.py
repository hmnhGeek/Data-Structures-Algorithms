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

    def count_subsets(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(count_subsets([1, 2, 2, 3], 3))
    print(count_subsets([1, 1, 4, 5], 5))
    print(count_subsets([2, 34, 5], 40))

recursive()