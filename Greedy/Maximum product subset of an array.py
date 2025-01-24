class Solution:
    @staticmethod
    def get_max_product(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # store the count of zeros and negative numbers in the array
        zero_count = negative_count = 0

        # store the max negative number (which could be required as we will see).
        max_negative = -1e6

        # store the product
        product = 1

        # loop in the array
        for i in range(len(arr)):
            # if ith element is 0, increment zero count and continue, i.e., don't include 0 in product.
            if arr[i] == 0:
                zero_count += 1
                continue

            # if ith element is negative, increment negative count and update the max negative.
            elif arr[i] < 0:
                negative_count += 1
                max_negative = max(max_negative, arr[i])

            # if the number is positive or negative, include it in the product.
            product *= arr[i]

        # if all the elements were 0, return 0 and not 1.
        if zero_count == len(arr):
            return 0

        # if there was only 1 negative and rest 0s, then also, max product will be 0. If however, negatives were, say, 3
        # and rest were 0s, then 2 negative numbers could make a positive product > 0, thus we only return a 0 in this
        # case.
        if negative_count == 1 and zero_count + negative_count == len(arr):
            return 0

        # if the negative count is odd, we must divide the product by max negative (nearest negative to 0 on number
        # line) to obtain the max positive product.
        if negative_count % 2 == 1:
            product = product // max_negative

        # return the product.
        return product


print(Solution.get_max_product([-1, -1, -2, 4, 3]))
print(Solution.get_max_product([-1, 0]))
print(Solution.get_max_product([5]))
