# Problem link - https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings
# Solution - https://www.youtube.com/watch?v=qN_vwYtvFUM


def check_shuffle(s1: str, s2: str, s3: str):
    """
        Time complexity is O(max(n1, n2, n3)) and space complexity is O(1).
    """

    n1, n2, n3 = len(s1), len(s2), len(s3)

    # if the sum of lengths don't match with n3, return False.
    if n1 + n2 != n3:
        return False

    # start iterating on all the strings.
    i, j, k = 0, 0, 0
    while k < n3:
        # if strings s1 and s3 match at `i`, increment `i`.
        if i < n1 and s1[i] == s3[k]:
            i += 1
        # if strings s2 and s3 match at `j`, increment `j`.
        elif j < n2 and s2[j] == s3[k]:
            j += 1
        # if both of them don't match, return a False, as the order is not correct.
        else:
            return False
        # increment `k` also finally.
        k += 1

    # if after completing the traversal on s3, either of s1 or s2 is left, return False.
    if i < n1 or j < n2:
        return False

    # return True, as the s3 string is correct shuffle of both s1 and s2 strings.
    return True


print(check_shuffle("xy", "12", "1x2y"))
print(check_shuffle("xy", "12", "y1x2"))
print(check_shuffle("xy", "12", "y21xx"))
print(check_shuffle("abdd", "fef", "abfddef"))
print(check_shuffle("aab", "abc", "aabbc"))
print(check_shuffle("zxry", "qwr", "qwzxxryr"))
print(check_shuffle("a", "a", "aa"))