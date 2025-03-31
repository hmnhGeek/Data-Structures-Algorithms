# Problem link - https://www.naukri.com/code360/problems/longest-bitonic-sequence_1062688?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=y4vN0WNdrlg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=47


def get_longest_increasing_subsequence(arr):
    n = len(arr)
    dp = {i: 1 for i in range(n)}
    parents = {i: i for i in range(n)}
    for index in range(n):
        for prev in range(index):
            if arr[index] > arr[prev] and dp[index] < 1 + dp[prev]:
                dp[index] = 1 + dp[prev]
                parents[index] = prev
    return list(dp.values()), list(parents.values())


def fill_part(start_index, parents, arr, result):
    while parents[start_index] != start_index:
        result.append(arr[start_index])
        start_index = parents[start_index]
    result.append(arr[start_index])


def longest_bi_tonic(arr):
    """
        Overall time complexity is O(n^2) and space complexity is O(n).
    """

    n = len(arr)

    # get the lis and parents array for the given array `arr` in O(n^2) time and O(n) space.
    dp1, p1 = get_longest_increasing_subsequence(arr)

    # get the lis and parents array for the given array's reversed form in O(n^2) time and O(n) space.
    # Basically, we are trying to get the lis from right side.
    dp2, p2 = get_longest_increasing_subsequence(arr[-1:-len(arr)-1:-1])

    # lis array could be simply reversed to get the correct right side lis dp.
    dp2 = dp2[-1:-len(dp2)-1:-1]

    # however, for parents, we need to invert the indices first before reversing it.
    p2 = [n - i - 1 for i in p2]
    p2 = p2[-1:-len(p2)-1:-1]

    # get the length of bi-tonic subsequences. (-1 for overlapping peak index).
    summed = [dp1[i] + dp2[i] - 1 for i in range(n)]

    # get the max value index from the summed bi-tonic array dp.
    peak_index = summed.index(max(summed))

    # fill the increasing and decreasing elements.
    increasing_part = []
    decreasing_part = []
    fill_part(peak_index, p1, arr, increasing_part)
    fill_part(peak_index, p2, arr, decreasing_part)

    # to get the increasing part, just like in our previous LIS questions, reverse it, but before reversing, let's
    # remove 0th index from the increasing part because it's a peak index value which would also be found in decreasing
    # part.
    increasing_part = increasing_part[1:]
    increasing_part = increasing_part[-1:-len(increasing_part)-1:-1]

    # extend increasing part by adding the decreasing part and return it. This is the correct longest length bi-tonic
    # subsequence. Note that we don't need to reverse the decreasing part.
    increasing_part.extend(decreasing_part)
    return increasing_part


print(longest_bi_tonic([1, 11, 2, 10, 4, 5, 2, 1]))
print(longest_bi_tonic([1, 2, 1, 2, 1]))
print(longest_bi_tonic([1, 2, 1, 3, 4]))
print(longest_bi_tonic([12, 11, 40, 5, 3, 1]))
print(longest_bi_tonic([80, 60, 30]))
print(longest_bi_tonic([10, 10, 10]))