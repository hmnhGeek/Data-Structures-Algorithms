# Problem link - https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
# Solution - https://www.youtube.com/watch?v=xmguZ6GbatA&t=648s


class Solution:
    @staticmethod
    def subarray_with_0_sum(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # define a dictionary to store the indices of the prefix sums. Note that we have explicitly added prefix sum 0
        # with index -1 to denote the starting of the array.
        d = {0: -1}

        # store sum tracker and max length
        _sum = 0
        max_length = 0

        # store the starting index of the sub array.
        start_index = -1

        # loop in the array
        for i in range(len(arr)):
            _sum += arr[i]
            # if the sum is in the array as prefix sum, then arr[d[_sum] + 1 : i + 1] subarray will have a sum 0.
            # Therefore, update the result variables.
            if _sum in d:
                start_index = d[_sum] + 1
                max_length = i - d[_sum]
            else:
                # else, assign this prefix sum in the dictionary.
                d[_sum] = i

        # return the subarray.
        return arr[start_index:start_index+max_length] if start_index != -1 else []


print(Solution.subarray_with_0_sum([4, 2, -3, 1, 6]))
print(Solution.subarray_with_0_sum([9, -3, 3, -1, 6, -5]))
print(Solution.subarray_with_0_sum([4, 2, 0, 1, 6]))
print(Solution.subarray_with_0_sum([1, 4, -5]))
print(Solution.subarray_with_0_sum([1, 3, -1, 4, -4]))
print(Solution.subarray_with_0_sum([1, -1, 2, -2]))
print(Solution.subarray_with_0_sum([1, 2, 1, -2]))
