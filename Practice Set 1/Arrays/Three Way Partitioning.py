class Solution:
    @staticmethod
    def three_way_partitioning(arr, a, b):
        low, high = 0, len(arr) - 1
        mid = 0
        while mid <= high:
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1
            elif arr[mid] > b:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            else:
                mid += 1
        print(arr)


Solution.three_way_partitioning([1, 2, 3, 3, 4], 1, 2)
Solution.three_way_partitioning([1, 4, 3, 6, 2, 1], 1, 3)