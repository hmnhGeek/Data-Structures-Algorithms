class Solution:
    @staticmethod
    def _find_product_except(arr, index=None):
        product = 1
        multiplication_done = False
        for i in range(len(arr)):
            if i != index:
                product *= arr[i]
                multiplication_done = True
        return product if multiplication_done else 0

    @staticmethod
    def get_product_array(arr):
        n = len(arr)
        result = [0] * n
        count_of_zeros = 0
        last_index_of_zero = None
        for i in range(n):
            if arr[i] == 0:
                count_of_zeros += 1
                last_index_of_zero = i
        if count_of_zeros == 0:
            full_product = Solution._find_product_except(arr)
            for i in range(n):
                result[i] = full_product // arr[i]
        elif count_of_zeros == 1:
            result[last_index_of_zero] = Solution._find_product_except(arr, last_index_of_zero)
        return result


print(Solution.get_product_array([12, 0]))
print(Solution.get_product_array([10, 3, 5, 6, 2]))
print(Solution.get_product_array([0]))
print(Solution.get_product_array([1, 2, 3, 4, 5]))
print(Solution.get_product_array([-1, 1, 0, -3, 3]))
print(Solution.get_product_array([1, 2, 3, 4]))
print(Solution.get_product_array([1, 3, 3, 10, 2]))
print(Solution.get_product_array([2, 4, 6, 3, 1, 1]))
print(Solution.get_product_array([1, 10, 1, 2, 2]))
print(Solution.get_product_array([2, 12, 1, 1, 20, 1]))
