# Problem link - https://www.geeksforgeeks.org/problems/binary-subarray-with-sum/0
# Solution - https://www.youtube.com/watch?v=XnMdNUkX6VM&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


class Solution:
    @staticmethod
    def _binary_sum_subarray(arr, k):
        """
            The idea is to find the count of substrings where the sum of each substring <= k and not exactly k.
        """

        # if k is negative, return 0.
        if k < 0:
            return 0

        # define window variables.
        left = right = 0
        n = len(arr)
        count_less_than_equal_to_k = 0
        window_sum = 0

        # while there is ground to cover.
        while right < n:
            # add the current right indexed element into window sum.
            window_sum += arr[right]

            # till the window sum is greater than k (i.e., not <= k), continue shrinking from the left side. Here we
            # don't want to maintain the longest window size, therefore a while loop is needed and a simple if condition
            # will not work.
            while window_sum > k:
                window_sum -= arr[left]
                left += 1

            # update the count and increment right.
            count_less_than_equal_to_k += (right - left + 1)
            right += 1

        # return the final count.
        return count_less_than_equal_to_k

    @staticmethod
    def binary_sum_subarray(arr, k):
        """
            The idea is that in a binary array, the sum == k can be found out using the formula:
                f(sum = k) = f(sum <= k) - f(sum <= k-1)

            Overall time complexity is O(2n) and space complexity is O(1).
        """
        return Solution._binary_sum_subarray(arr, k) - Solution._binary_sum_subarray(arr, k - 1)


print(Solution.binary_sum_subarray([1, 0, 1, 0, 1], 2))
print(Solution.binary_sum_subarray([0]*5, 0))
print(Solution.binary_sum_subarray([1, 0, 1, 1, 0, 1], 2))
print(Solution.binary_sum_subarray([1, 0, 1, 1, 1, 0, 1], 3))
print(Solution.binary_sum_subarray([1, 1, 0, 1, 1], 5))
