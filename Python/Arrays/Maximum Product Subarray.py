# Problem link - https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1
# Solution - https://www.youtube.com/watch?v=hnswaLJvr6g


class Solution:
    @staticmethod
    def get_max_product(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define prefix as the product obtained by traversing from the front of the array and suffix as the product
        # obtained by traversing from the end of the array. For starting, set both of them to 1.
        prefix = suffix = 1

        # set max product of the subarray as -inf.
        max_product = -1e6

        # loop on the array
        n = len(arr)
        for i in range(n):
            # if at any time, prefix has become 0, reset it to 1. Basically, arr[i] = 0 will make prefix = 0. That means
            # we have reached a breakpoint. From next `i`, a new subarray will start.
            if prefix == 0:
                prefix = 1

            # same logic as prefix = 0, but this time from the back side.
            if suffix == 0:
                suffix = 1

            # update prefix and suffix and take the max product.
            prefix = prefix * arr[i]
            suffix = suffix * arr[n - i - 1]
            max_product = max(max_product, prefix, suffix)

        # return the max product of the subarray.
        return max_product


print(Solution.get_max_product([-2, 6, -3, -10, 0, 2]))
print(Solution.get_max_product([-1, -3, -10, 0, 6]))
print(Solution.get_max_product([2, 3, 4]))
print(Solution.get_max_product([2, 3, -2, 4]))
print(Solution.get_max_product([-2, 0, -1]))
print(Solution.get_max_product([-1, -3, -10, 0, 60]))
