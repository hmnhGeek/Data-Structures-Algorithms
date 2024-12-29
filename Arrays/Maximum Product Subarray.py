class Solution:
    @staticmethod
    def get_max_product(arr):
        prefix = suffix = 1
        max_product = -1e6
        n = len(arr)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix * arr[i]
            suffix = suffix * arr[n - i - 1]
            max_product = max(max_product, prefix, suffix)
        return max_product


print(Solution.get_max_product([-2, 6, -3, -10, 0, 2]))
print(Solution.get_max_product([-1, -3, -10, 0, 6]))
print(Solution.get_max_product([2, 3, 4]))
print(Solution.get_max_product([2,3,-2,4]))
print(Solution.get_max_product([-2,0,-1]))
print(Solution.get_max_product([-1, -3, -10, 0, 60]))