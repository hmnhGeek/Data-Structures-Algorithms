def recursive():
    def solve(arr, index, target):
        if target == 0:
            return 0

        if index == 0:
            return target // arr[0] if target % arr[0] == 0 else 1e6

        left = 1e6
        if target >= arr[index]:
            left = 1 + solve(arr, index, target - arr[index])
        right = solve(arr, index - 1, target)
        return min(left, right)

    def minimum_coins(denominations, amount):
        num_denominations = len(denominations)
        num_coins = solve(denominations, num_denominations - 1, amount)
        return num_coins if num_coins != 1e6 else -1

    print(minimum_coins([1, 2, 3], 7))
    print(minimum_coins([12, 1, 3], 4))
    print(minimum_coins([1, 2], 11))
    print(minimum_coins([25, 10, 5], 30))
    print(minimum_coins([9, 6, 5, 1], 19))
    print(minimum_coins([5, 1], 0))
    print(minimum_coins([4, 6, 2], 5))


recursive()