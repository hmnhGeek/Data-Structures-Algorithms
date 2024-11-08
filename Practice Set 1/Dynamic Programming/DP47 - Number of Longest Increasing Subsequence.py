# Problem link - https://www.naukri.com/code360/problems/number-of-longest-increasing-subsequence_3751627?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=cKVl1TFdNXg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=48


from typing import List


class Solution:
    @staticmethod
    def get_number_of_lis(arr: List[int]) -> int:
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        n = len(arr)

        # create dp and count arrays
        dp = {i: 1 for i in range(len(arr))}
        counts = {i: 1 for i in range(len(arr))}

        # loop on each index
        for index in range(n):
            # take all prev indices till this index.
            for prev in range(index):
                # if the current index is greater than prev index
                if arr[index] > arr[prev]:
                    # and if dp[index] < 1 + dp[prev], then basically, you have got a longer increasing subsequence now.
                    # Update dp[index] and set the count[index] to the count[prev] because that's the longest you can
                    # start with now.
                    if dp[index] < 1 + dp[prev]:
                        dp[index] = 1 + dp[prev]
                        counts[index] = counts[prev]
                    # if however, the relation is equality, then just take the count from prev and add it.
                    elif dp[index] == 1 + dp[prev]:
                        counts[index] += counts[prev]

        # get the length of LIS and sum up all the counts which where length from dp is equal to length of LIS.
        lis_length = max(dp.values())
        num_lis = 0
        for i in dp:
            if dp[i] == lis_length:
                num_lis += counts[i]

        # return the number of LIS.
        return num_lis


print(Solution.get_number_of_lis([50, 3, 90, 60, 80]))
print(Solution.get_number_of_lis([3, 7, 4, 6]))
print(Solution.get_number_of_lis([5, 7, 2, 3]))
print(Solution.get_number_of_lis([1, 5, 4, 3, 2, 6, 7, 10, 8, 9]))
print(Solution.get_number_of_lis([1, 3, 5, 4, 7]))
print(Solution.get_number_of_lis([2, 2, 2, 2, 2]))
