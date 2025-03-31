# Problem link - https://www.naukri.com/code360/problems/longest-string-chain_3752111?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=YY8iBaYcc4g&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=46


from typing import List
from collections import Counter


def custom_string_compare(s1: str, s2: str) -> bool:
    """
        Time complexity is O(n) and space complexity is O(n).
    """

    n1, n2 = len(s1), len(s2)
    if abs(n1 - n2) != 1:
        return False

    d1, d2 = Counter(s1), Counter(s2)

    # start a check from d1. Will take O(n) time.
    for char in d1:
        # if the character is present in d1 (<> 0) and also in d2 (<> 0), delete from both.
        if char in d2 and d1[char] > 0:
            d1[char] -= 1
            if d2[char] > 0:
                d2[char] -= 1

    # do exactly the same from d2's side. Additional O(n) time.
    for char in d2:
        if char in d1 and d2[char] > 0:
            d2[char] -= 1
            if d1[char] > 0:
                d1[char] -= 1

    # get all the non-zeros in dictionaries in O(n) time.
    d1 = {k: v for k, v in d1.items() if v != 0}
    d2 = {k: v for k, v in d2.items() if v != 0}
    if len(d1) == 0:
        return len(d2) == 1
    if len(d2) == 0:
        return len(d1) == 1
    return False


def get_longest_string_chain(strings: List[str]):
    n = len(strings)
    dp = {i: 1 for i in range(n)}
    parents = {i: i for i in range(n)}

    # Sorting is necessary because the question is not asking for subsequence, but subset,
    # so any order can be picked from the strings. Sorting will ensure that the list maintains
    # increasing length strings.
    strings.sort(key=len)

    for index in range(n):
        for prev in range(index):
            if custom_string_compare(strings[index], strings[prev]):
                if dp[index] < 1 + dp[prev]:
                    dp[index] = 1 + dp[prev]
                    parents[index] = prev

    return max(dp.values())


print(get_longest_string_chain(["x", "xx", "y", "xyx"]))
print(get_longest_string_chain(["m", "nm", "mmm"]))
print(get_longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))
print(get_longest_string_chain(["a","b","ba","bca","bda","bdca"]))
print(get_longest_string_chain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))