class Solution:
    @staticmethod
    def get_max_points(arr, k):
        n = len(arr)
        if k not in range(1, n + 1):
            return -1
        i, j = k - 1, n
        max_sum, t = sum(arr[:k]), sum(arr[:k])
        while i >= 0:
            t -= arr[i]
            t += arr[j - 1]
            if max_sum < t:
                max_sum = t
            i -= 1
            j -= 1
        return max_sum


print(Solution.get_max_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.get_max_points([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.get_max_points([2, 2, 2], 2))
print(Solution.get_max_points([8, 6, 2, 4, 5], 5))
