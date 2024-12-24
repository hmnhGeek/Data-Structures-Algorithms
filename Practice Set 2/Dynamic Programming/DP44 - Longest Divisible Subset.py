def get_at(arr, index):
    if index >= len(arr):
        return 1
    if index < 0:
        return 1
    return arr[index]


def mutual_divisibility(arr, index, prev_index):
    return get_at(arr, prev_index) % get_at(arr, index) == 0 or get_at(arr, index) % get_at(arr, prev_index) == 0


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, index, prev_index):
        if index == 0:
            return 1 if mutual_divisibility(arr, 0, prev_index) else 0
        left = 0
        if mutual_divisibility(arr, index, prev_index):
            left = 1 + solve(arr, index - 1, index)
        right = solve(arr, index - 1, prev_index)
        return max(left, right)

    def lds(arr):
        n = len(arr)
        return solve(arr, n - 1, n)

    print(lds([1, 16, 7, 8, 4]))
    print(lds([1, 2, 5]))
    print(lds([3, 3, 3]))
    print(lds([1, 2, 4, 8]))
    print(lds([1, 2, 3]))
    print(lds([2, 4, 3, 8]))


recursive()
