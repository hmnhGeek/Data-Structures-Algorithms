# Problem link - https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    @staticmethod
    def _find_product_except(arr, index=None):
        product = 1
        # assume that arr = [0], check what will happen if `multiplication_done` variable is not used.
        multiplication_done = False

        # in O(n) time, get the product of all the indices except index = `index`.
        for i in range(len(arr)):
            if i != index:
                product *= arr[i]
                multiplication_done = True
        return product if multiplication_done else 0

    @staticmethod
    def get_product_array(arr):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # store the length of the array.
        n = len(arr)

        # create a result array with all 0s of length n. This will take O(n) space.
        result = [0] * n

        # get the count of zeros in the array with the index of last 0. If count comes out to be 1, then the last index
        # will be the index of the only 0 itself, and we require this index in this case only. This will take O(n) time.
        count_of_zeros = 0
        last_index_of_zero = None
        for i in range(n):
            if arr[i] == 0:
                count_of_zeros += 1
                last_index_of_zero = i

        # if there are no zeros in the array, do this in O(2n) time.
        if count_of_zeros == 0:
            # then simply find the product of all the elements in the array in O(n) time.
            full_product = Solution._find_product_except(arr)
            # and modify result array by dividing the product with ith element from the array, in another O(n) time.
            for i in range(n):
                result[i] = full_product // arr[i]

        # however, if there is exactly one zero in the array
        elif count_of_zeros == 1:
            # only at the index of that zero with the product be non-zero, else all other elements will have a 0
            # product. Therefore, calculate the product from the array except using the 0. This will also take O(n)
            # time.
            result[last_index_of_zero] = Solution._find_product_except(arr, last_index_of_zero)

        # else case is not required, which is that if there are more than 1 zero. In that case, each element will have
        # in its product at least 1 zero, therefore, the original list having all 0s will also work and thus no need for
        # any explicit else condition. Return the result.
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

print()


class OptimalSolution:
    @staticmethod
    def _populate_prefix_into_result(arr, result, n):
        prefix = 1
        for i in range(n):
            # assign ith index with prefix
            result[i] = prefix
            # update prefix for next `i` as prefix * arr[i] as this element will be added into the product for the next
            # `i` index.
            prefix *= arr[i]

    @staticmethod
    def _populate_postfix_into_result(arr, result, n):
        postfix = 1
        # this time traverse from the right side.
        for i in range(n - 1, -1, -1):
            # multiply with postfix value at index `i`.
            result[i] *= postfix
            # update postfix for next `i` as prefix * arr[i] as this element will be added into the product for the next
            # `i` index.
            postfix *= arr[i]

    @staticmethod
    def get_product_array(arr):
        """
            Time complexity is O(n) and space complexity is O(n). However, special case [0] is not handled.
        """

        n = len(arr)
        # create a result array with O(n) space.
        result = [None]*n
        # populate the result array with prefix product in O(n) time.
        OptimalSolution._populate_prefix_into_result(arr, result, n)
        # populate the result array with prefix * postfix product in O(n) time.
        OptimalSolution._populate_postfix_into_result(arr, result, n)
        # finally result will have the final answer.
        return result


print(OptimalSolution.get_product_array([12, 0]))
print(OptimalSolution.get_product_array([10, 3, 5, 6, 2]))
print(OptimalSolution.get_product_array([0]))
print(OptimalSolution.get_product_array([1, 2, 3, 4, 5]))
print(OptimalSolution.get_product_array([-1, 1, 0, -3, 3]))
print(OptimalSolution.get_product_array([1, 2, 3, 4]))
print(OptimalSolution.get_product_array([1, 3, 3, 10, 2]))
print(OptimalSolution.get_product_array([2, 4, 6, 3, 1, 1]))
print(OptimalSolution.get_product_array([1, 10, 1, 2, 2]))
print(OptimalSolution.get_product_array([2, 12, 1, 1, 20, 1]))
