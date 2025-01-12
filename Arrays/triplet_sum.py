class Solution:
    @staticmethod
    def is_present(arr, target):
        arr.sort()
        n = len(arr)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                _sum = arr[i] + arr[j] + arr[k]
                if _sum == target:
                    return True
                if _sum > target:
                    k -= 1
                else:
                    j += 1
        return False


print(Solution.is_present([1, 4, 45, 6, 10, 8], 13))
print(Solution.is_present([1, 2, 4, 3, 6, 7], 10))
print(Solution.is_present([40, 20, 10, 3, 6, 7], 24))
