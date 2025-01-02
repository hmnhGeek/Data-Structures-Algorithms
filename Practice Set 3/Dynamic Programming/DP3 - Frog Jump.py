def recursive():
    def solve(arr, index):
        """
            Time complexity is O(2^n) and space complexity is O(n).
        """

        if index == 0:
            return 0

        left = 1e6
        if index - 1 >= 0:
            left = abs(arr[index] - arr[index - 1]) + solve(arr, index - 1)
        right = 1e6
        if index - 2 >= 0:
            right = abs(arr[index] - arr[index - 2]) + solve(arr, index - 2)
        return min(left, right)

    def frog_jump(arr):
        n = len(arr)
        return solve(arr, n - 1)

    print(frog_jump([30, 10, 60, 10, 60, 50]))
    print(frog_jump([10, 20, 30, 10]))
    print(frog_jump([10, 50, 10]))
    print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))
    print(frog_jump([4, 8, 3, 10, 4, 4]))
    print(frog_jump([30, 20, 50, 10, 40]))


recursive()