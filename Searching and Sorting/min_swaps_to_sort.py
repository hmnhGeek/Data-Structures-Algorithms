class Solution:
    @staticmethod
    def find_min_swaps(arr):
        n = len(arr)
        temp = [(arr[i], i) for i in range(n)]
        temp.sort(key=lambda x: x[0])
        swaps_count = 0
        i = 0
        while i < n:
            while temp[i][1] != i:
                idx = temp[i][1]
                temp[i], temp[idx] = temp[idx], temp[i]
                swaps_count += 1
            i += 1
        return swaps_count


print(Solution.find_min_swaps([10, 19, 6, 3, 5]))
print(Solution.find_min_swaps([6, 3, 1, 2, 4, 5]))