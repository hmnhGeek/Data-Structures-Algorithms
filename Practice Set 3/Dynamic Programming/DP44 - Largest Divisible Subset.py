def is_divisible(arr, index1, index2):
    if index2 >= len(arr) or index1 >= len(arr):
        return True
    return arr[index1] % arr[index2] == 0 or arr[index2] % arr[index1] == 0


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, i, j):
        if i == 0:
            return is_divisible(arr, 0, j)
        left = -1e6
        if is_divisible(arr, i, j):
            left = 1 + solve(arr, i - 1, i)
        right = solve(arr, i - 1, j)
        return max(left, right)
    
    def largest_divisible_subset(arr):
        n = len(arr)
        return solve(arr, n - 1, n)

    print(largest_divisible_subset([1, 16, 7, 8, 4]))
    print(largest_divisible_subset([1, 2, 5]))
    print(largest_divisible_subset([3, 3, 3]))
    print(largest_divisible_subset([1, 2, 4, 8]))
    print(largest_divisible_subset([1, 2, 3]))
    print(largest_divisible_subset([2, 4, 3, 8]))


recursive()