def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def min_coins(arr, target):
        n = len(arr)
        coins = solve(arr, n - 1, target)
        if coins == 1e6:
            return -1
        return coins

    def solve(arr, i, j):
        if j == 0:
            return 0
        if i == 0:
            if j % arr[0] == 0:
                return j // arr[0]
            return 1e6
        left = 1e6
        if j >= arr[i]:
            left = 1 + solve(arr, i, j - arr[i])
        right = solve(arr, i - 1, j)
        return min(left, right)

    print(min_coins([1, 2, 3], 7))
    print(min_coins([1], 0))
    print(min_coins([12, 1, 3], 4))
    print(min_coins([2, 1], 11))
    print(min_coins([1, 2, 5], 11))
    print(min_coins([2], 3))
    print(min_coins([1, ], 0))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))


recursive()
print()
