from typing import List
from collections import Counter


def custom_string_compare(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if abs(n1 - n2) != 1:
        return False

    d1, d2 = Counter(s1), Counter(s2)
    for char in d1:
        if char in d2 and d1[char] > 0:
            if d1[char] > 0:
                d1[char] -= 1
            if d2[char] > 0:
                d2[char] -= 1

    for char in d2:
        if char in d1 and d2[char] > 0:
            if d2[char] > 0:
                d2[char] -= 1
            if d1[char] > 0:
                d1[char] -= 1

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