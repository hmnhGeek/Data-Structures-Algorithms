class Solution:
    @staticmethod
    def get_max_product(arr):
        zero_count = negative_count = 0
        max_negative = -1e6
        product = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_count += 1
                continue
            elif arr[i] < 0:
                negative_count += 1
                max_negative = max(max_negative, arr[i])
            product *= arr[i]
        if zero_count == len(arr):
            return 0
        if negative_count == 1 and zero_count + negative_count == len(arr):
            return 0
        if negative_count % 2 == 1:
            product = product // max_negative
        return product


print(Solution.get_max_product([-1, -1, -2, 4, 3]))
print(Solution.get_max_product([-1, 0]))