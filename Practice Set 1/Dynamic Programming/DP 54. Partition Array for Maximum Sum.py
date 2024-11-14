def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, index, k, n):
        if index == n:
            return 0
        ans = -1e6
        length = 0
        max_elem = -1e6
        for j in range(index, min(n, index + k)):
            length += 1
            max_elem = max(max_elem, arr[j])
            s = (length * max_elem) + solve(arr, j + 1, k, n)
            ans = max(ans, s)
        return ans

    def partition_for_max_sum(arr, k):
        n = len(arr)
        return solve(arr, 0, k, n)

    print(partition_for_max_sum([1, 15, 7, 9, 2, 5, 10], 3))
    print(partition_for_max_sum([1,4,1,5,7,3,6,1,9,9,3], 4))
    print(partition_for_max_sum([1], 1))


recursive()
