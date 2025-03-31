# Problem link - https://www.geeksforgeeks.org/find-the-length-of-the-longest-possible-word-chain/
# Solution - https://www.youtube.com/watch?v=YY8iBaYcc4g&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=46


def chain_possible(x, y):
    if len(x) != len(y) + 1:
        return False
    i, j = 0, 0
    while i < len(x):
        if 0 <= j < len(y) and x[i] == y[j]:
            j += 1
        i += 1
    return i == len(x) and j == len(y)


def longest_string_chain(strings):
    """
        Overall time complexity is O(n^2 * l) and space complexity is O(n).
    """

    # sort the strings array by length in O(n log(n)) time.
    strings.sort(key=len)

    # store dp and parents dictionary in O(n) space.
    dp = {i: 1 for i in range(len(strings))}
    parents = {i: i for i in range(len(strings))}

    # loop on i and j in O(n^2) time
    for i in range(len(strings)):
        for j in range(i):
            # assuming strings[i] to be larger, we are taking another O(l) time to check if chain is possible or not,
            # where l is the length of strings[i].
            if chain_possible(strings[i], strings[j]) and dp[i] < 1 + dp[j]:
                dp[i] = 1 + dp[j]
                parents[i] = j

    # back track to get the longest chain.
    start_index = max(dp, key=dp.get)
    result = []
    while start_index != parents[start_index]:
        result.append(strings[start_index])
        start_index = parents[start_index]
    result.append(strings[start_index])
    return result[-1:-len(result) - 1:-1]


print(longest_string_chain(["x", "xx", "y", "xyx"]))
print(longest_string_chain(["m", "nm", "mmm"]))
print(longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))
print(longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(longest_string_chain(["abcd", "dbqca"]))
