# Problem link - https://www.geeksforgeeks.org/problems/minimum-swaps/1
# Solution - https://www.youtube.com/watch?v=kFe_LRWuZjE


class Solution:
    @staticmethod
    def find_min_swaps(arr):
        """
            Time complexity is O(nlog(n)) and space complexity is O(n).
        """

        n = len(arr)

        # construct n-sized temp array storing the element and its index in a tuple format from the original array. This
        # will take O(n) time and O(n) space.
        temp = [(arr[i], i) for i in range(n)]

        # sort the temp array based on the 0th element of each tuple, i.e., original elements, in O(n * log(n)) time.
        temp.sort(key=lambda x: x[0])

        # store the swaps count.
        swaps_count = 0

        # iterate on the temp array now in O(n) time. This is used to build back the given array.
        i = 0
        while i < n:
            # until the ith index has its correct tuple where tuple's 1st value points to i, do the following.
            while temp[i][1] != i:
                # get the index with which we should swap
                idx = temp[i][1]
                # perform the swap
                temp[i], temp[idx] = temp[idx], temp[i]
                # increment the swap value
                swaps_count += 1
            # once the correct tuple is at i, move to next i.
            i += 1

        # return swaps count.
        return swaps_count


print(Solution.find_min_swaps([10, 19, 6, 3, 5]))
print(Solution.find_min_swaps([6, 3, 1, 2, 4, 5]))
print(Solution.find_min_swaps([1, 3, 4, 5, 6]))
print(Solution.find_min_swaps([2, 8, 5, 4]))
