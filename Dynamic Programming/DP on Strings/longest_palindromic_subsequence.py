# Problem link - https://leetcode.com/problems/longest-palindromic-subsequence/
# Solution - https://www.youtube.com/watch?v=6i_T5kkfv4A&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=30

# The main logic functions are from the longest common subsequence's space optimized solutions. Please refer them.
# Time complexity is O(N^2) and space complexity is O(N) as both strings will have same lengths.

def get_longest_common_subsequence(string1, string2):
    smaller_string = min(string1, string2, key=len)
    larger_string = max(string1, string2, key=len)

    n, m = len(larger_string), len(smaller_string)
    prev = {j: 0 for j in range(m)}
    prev[0] = 1 if string1[0] == string2[0] else 0

    for index2 in range(1, m):
        prev[index2] = 1 if string1[0] == string2[index2] else prev[index2 - 1]

    for index1 in range(1, n):
        curr = {j: 0 for j in range(m)}
        curr[0] = 1 if string1[index1] == string2[0] else prev[0]
        for index2 in range(1, m):
            if string1[index1] == string2[index2]:
                curr[index2] = 1 + prev[index2 - 1]
            else:
                curr[index2] = max(prev[index2], curr[index2 - 1])
        prev = curr
    return prev[m - 1]


def _print_longest_common_subsequence(string1, string2):
    smaller_string = min(string1, string2, key=len)
    larger_string = max(string1, string2, key=len)

    n, m = len(larger_string), len(smaller_string)
    prev = {j: "" for j in range(m)}
    prev[0] = string1[0] if string1[0] == string2[0] else ""

    for index2 in range(1, m):
        prev[index2] = string1[0] if string1[0] == string2[index2] else prev[index2 - 1]

    for index1 in range(1, n):
        curr = {j: 0 for j in range(m)}
        curr[0] = string2[0] if string1[index1] == string2[0] else prev[0]
        for index2 in range(1, m):
            if string1[index1] == string2[index2]:
                curr[index2] = prev[index2 - 1] + string1[index1]
            else:
                curr[index2] = max(prev[index2], curr[index2 - 1], key=len)
        prev = curr
    return prev[m - 1]


def get_length_of_longest_palindromic_subsequence(string):
    reversed_string = string[-1:-len(string) - 1:-1]
    return get_longest_common_subsequence(string, reversed_string)


def print_longest_palindromic_subsequence(string):
    reversed_string = string[-1:-len(string) - 1: -1]
    return _print_longest_common_subsequence(string, reversed_string)


print(get_length_of_longest_palindromic_subsequence("bbbab"))
print(print_longest_palindromic_subsequence("bbbab"))
print()

print(get_length_of_longest_palindromic_subsequence("cbbd"))
print(print_longest_palindromic_subsequence("cbbd"))
print()

print(get_length_of_longest_palindromic_subsequence("GEEKSFORGEEKS"))
print(print_longest_palindromic_subsequence("GEEKSFORGEEKS"))
print()

print(get_length_of_longest_palindromic_subsequence("BBABCBCAB"))
print(print_longest_palindromic_subsequence("BBABCBCAB"))
print()
