# Problem link - https://www.naukri.com/code360/problems/number-of-longest-increasing-subsequence_3751627?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=cKVl1TFdNXg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=48


def get_num_longest_increasing_subsequence(arr):
    # The time complexity O(n^2) and space complexity is O(n).
    n = len(arr)

    # create counts and dp array to store the lengths of LIS at index i and the length of LIS at index i.
    counts = {i: 1 for i in range(n)}
    dp = {i: 1 for i in range(n)}

    for i in range(n):
        for prev in range(i):
            # if the prev is lower than current, and you can achieve more length, then update the dp[i]
            # and also update the counts[i] to the counts[prev] because the number of LIS at prev index
            # can same be used to form LIS at index i.
            if arr[i] > arr[prev] and dp[prev] + 1 > dp[i]:
                dp[i] = dp[prev] + 1
                counts[i] = counts[prev]
            # else if prev is lower than current, however, the LIS has same length even after using prev
            # then it means another LIS of dp[i] length can be made using prev. So increment the counts[i]
            # by "adding" counts[prev].
            elif arr[i] > arr[prev] and dp[prev] + 1 == dp[i]:
                counts[i] += counts[prev]

    # get the length of longest increasing subsequence
    longest_increasing_length = max(dp.values())
    # set the number of LIS to 0
    num_lis = 0

    # loop in the index range.
    for i in range(n):
        # if the LIS length at index i is same as longest_increasing_length, then add the counts[i]
        if dp[i] == longest_increasing_length:
            num_lis += counts[i]

    # return the number of LIS found.
    return num_lis


print(get_num_longest_increasing_subsequence([50, 3, 90, 60, 80]))
print(get_num_longest_increasing_subsequence([3, 7, 4, 6]))
print(get_num_longest_increasing_subsequence([5, 7, 2, 3]))
print(get_num_longest_increasing_subsequence([2, 2, 2, 2, 2]))
print(get_num_longest_increasing_subsequence([1, 3, 5, 4, 7]))