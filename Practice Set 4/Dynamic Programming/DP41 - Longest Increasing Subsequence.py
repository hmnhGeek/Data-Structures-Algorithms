def recursive():
    def solve(arr, index, prev):
        if index == 0:
            return 1 if arr[0] < prev else 0
        left = -1e6
        if arr[index] < prev:
            left = 1 + solve(arr, index - 1, arr[index])
        right = solve(arr, index - 1, prev)
        return max(left, right)

    def get_lis_length(arr):
        n = len(arr)
        return solve(arr, n - 1, 1e6)

    print(get_lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis_length([5, 4, 11, 1, 16, 8]))
    print(get_lis_length([1, 2, 2]))
    print(get_lis_length([0, 1, 0, 3, 2, 3]))
    print(get_lis_length([7, 7, 7, 7, 7, 7, 7]))
    print(get_lis_length([3, 10, 2, 1, 20]))
    print(get_lis_length([30, 20, 10]))
    print(get_lis_length([10, 20, 35, 80]))


recursive()