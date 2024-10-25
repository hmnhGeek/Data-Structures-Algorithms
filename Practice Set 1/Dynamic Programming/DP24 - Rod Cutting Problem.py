def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(prices, index, length):
        if length == 0:
            return 0

        if index == 1:
            return length * prices[0]

        left = 0
        if index <= length:
            left = prices[index - 1] + solve(prices, index, length - index)
        right = solve(prices, index - 1, length)
        return max(left, right)

    def rod_cut(prices, length):
        n = len(prices)
        return solve(prices, n, length)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))


recursive()