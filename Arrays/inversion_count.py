class Solution:
    @staticmethod
    def no_space(arr):
        count = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count += 1
        return count


print(Solution.no_space([2, 4, 1, 3, 5]))
print(Solution.no_space([2, 3, 4, 5, 6]))
print(Solution.no_space([10, 10, 10]))
print(Solution.no_space([4, 3, 2, 1]))
print(Solution.no_space([5, 4, 3, 2, 1]))
