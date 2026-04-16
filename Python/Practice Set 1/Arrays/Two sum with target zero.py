class Solution:
    @staticmethod
    def two_sum(arr):
        arr.sort()
        i = 0
        j = len(arr) - 1
        result = []
        while i < j:
            _sum = arr[i] + arr[j]
            if _sum == 0:
                result.append((arr[i], arr[j]))
                i += 1
                j -= 1
            elif _sum > 0:
                j -= 1
            else:
                i += 1
        return result


print(Solution.two_sum([-1, 0, 1, 2, -1, -4]))
print(Solution.two_sum([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))
