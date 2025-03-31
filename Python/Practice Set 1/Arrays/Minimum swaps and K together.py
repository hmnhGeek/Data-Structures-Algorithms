# Problem link - https://www.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1
# Solution - https://www.youtube.com/watch?v=0Hkh1cjnBNA


class Solution:
    @staticmethod
    def min_swaps(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # in O(n) time get the fixed window size required to solve this problem.
        n = len(arr)
        window_size = Solution._get_fixed_window_size(arr, k, n)

        # store the count of non-favourable (a_i > k) elements count.
        non_favs = 0

        # store the ans, i.e., min number of swaps required to group all the <= k numbers together.
        # The idea is to use a fixed window and find that particular window in which maximum <=k elements are grouped
        # together.
        ans = 1e6

        # count the non-favourable elements in first window.
        for i in range(window_size):
            if arr[i] > k:
                non_favs += 1

        # update the ans as minimum.
        ans = min(ans, non_favs)

        # get the starting end index.
        end_index = window_size - 1

        # loop till end_index < n - 1, because we will need end_index + 1 inside while.
        while end_index < n - 1:
            start_index = end_index - window_size + 1

            # if removing start_index removes one non-favourable element...
            if arr[start_index] > k:
                non_favs -= 1

            # increment start_index as we have removed start_index element.
            start_index += 1

            # add the end_index + 1 element in the window and increment non-favourable count if required.
            if arr[end_index + 1] > k:
                non_favs += 1

            # increment end_index.
            end_index += 1

            # update the ans.
            ans = min(ans, non_favs)

        # return the ans.
        return ans

    @staticmethod
    def _get_fixed_window_size(arr, k, n):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        result = 0
        for i in range(n):
            if arr[i] <= k:
                result += 1
        return result


print(Solution.min_swaps([2, 1, 5, 6, 3], 3))
print(Solution.min_swaps([2, 7, 9, 5, 8, 7, 4], 6))
print(Solution.min_swaps([2, 4, 5, 3, 6, 1, 8], 6))
print(Solution.min_swaps([5, 4, 6, 10, 35, 30, 8], 9))
print(Solution.min_swaps([1, 15, 18, 3, 14, 18, 5], 9))
print(Solution.min_swaps([1, 1, 5, 1, 2], 2))
print(Solution.min_swaps([1, 3, 2, 7, 7], 3))
print(Solution.min_swaps([5, 4, 3, 2, 6, 1], 6))
print(Solution.min_swaps([1, 2, 3, 7, 7, 2, 2], 2))
