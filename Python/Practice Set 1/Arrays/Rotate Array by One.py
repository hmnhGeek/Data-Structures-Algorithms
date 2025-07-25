class Solution:
    @staticmethod
    def rotate(arr):
        n = len(arr)
        last_elem = arr[-1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last_elem
        print(arr)


Solution.rotate([1, 2, 3, 4, 5])
Solution.rotate([9, 8, 7, 6, 4, 2, 1, 3])
