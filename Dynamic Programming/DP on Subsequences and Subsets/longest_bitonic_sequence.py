# Problem link - https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=y4vN0WNdrlg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=47


def get_length_of_longest_increasing_sequence(arr):
    # refer to this code's explanation in `printing_longest_increasing_subsequence.py` file.
    n = len(arr)
    dp = {i: 1 for i in range(n)}

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev] and 1 + dp[prev] > dp[i]:
                dp[i] = 1 + dp[prev]
    return dp


def get_longest_bitonic_sequence(arr):
    # Time complexity is O(n^2) and space complexity is O(n).

    n = len(arr)

    # get the longest increasing sequence in the array in O(n^2) time and O(n) space.
    dp1 = get_length_of_longest_increasing_sequence(arr)
    # get the longest increasing sequence in the reversed array in O(n^2) time and O(n) space.
    dp2 = get_length_of_longest_increasing_sequence(arr[-1:-len(arr)-1:-1])

    # calculate the lengths of bitonic sequence at each index being the peak by the formula
    # bitonic_length[i] = dp1[i] + dp2[i] - 1
    lengths = {i: dp1[i] + dp2[i] - 1 for i in range(n)}

    # return the max length of the bitonic sequence.
    return max(lengths.values())


print(get_longest_bitonic_sequence([1, 2, 1, 2, 1]))
print(get_longest_bitonic_sequence([1, 2, 1, 3, 4]))