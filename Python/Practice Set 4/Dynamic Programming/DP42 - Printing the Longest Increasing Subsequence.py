# Problem link - https://www.naukri.com/code360/problems/printing-longest-increasing-subsequence_8360670
# Solution - https://www.youtube.com/watch?v=IFfYfonAFGc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43


class Solution:
    @staticmethod
    def print_lis(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        n = len(arr)

        # create a dp and parents dictionaries to store the LIS length and the parents of each index respectively.
        dp = {i: 1 for i in range(n)}
        parents = {i: i for i in range(n)}

        # loop in the array
        for i in range(n):
            # loop for the previous index
            for prev in range(i):
                # if the prev index value can form an increasing subsequence with current index `i`.
                if arr[prev] < arr[i]:
                    # update the LIS length if possible and also update the parent.
                    if 1 + dp[prev] > dp[i]:
                        dp[i] = 1 + dp[prev]
                        parents[i] = prev

        # get the last index of LIS using the max value of dp.
        last_element_index_of_lis = max(dp, key=dp.get)

        # back track to form the LIS.
        j = last_element_index_of_lis
        lis = []
        while parents[j] != j:
            lis.append(arr[j])
            j = parents[j]
        lis.append(arr[j])

        # return the reverse of the backtracked array as the correct LIS.
        return lis[-1:-len(lis)-1:-1]


print(Solution.print_lis([5, 4, 11, 1, 16, 8]))
print(Solution.print_lis([1, 2, 2]))
print(Solution.print_lis([10, 20, 3, 40]))
print(Solution.print_lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(Solution.print_lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(Solution.print_lis([1]))
print(Solution.print_lis([5, 6, 3, 4, 7, 6]))
print(Solution.print_lis([1, 2, 3, 4, 5]))
