def recursive():
    """
        Time complexity is exponential and space complexity is O(n1 + n2)
    """

    def solve(s1: str, i: int, s2: str, j: int) -> bool:
        # if both the strings become empty at the same time, then strings have matched, return True.
        if i < 0 and j < 0:
            return True

        # if pattern string has exhausted, but not the other string, return False
        if i < 0 and j >= 0:
            return False

        # if pattern string is present, but the other string has exhausted...
        if i >= 0 and j < 0:
            # check for all the leftover characters in the pattern string
            for k in range(i, -1, -1):
                # if any character in the pattern is not a "*", return False, because if all of them are *s,
                # then only we can match the pattern string with an empty string.
                if s1[k] != "*":
                    return False
            return True

        # if characters from both strings match or the character in the pattern string is a "?", then there is a match,
        # call the recursion for next characters in both the strings.
        if s1[i] == s2[j] or s1[i] == "?":
            return solve(s1, i - 1, s2, j - 1)
        elif s1[i] == "*":
            # if the current character from the pattern string is a "*", then the * can match with either 0 characters
            # from the other string, or a number of continuous characters from the other string.

            # if we say that * does not match with any character in the other string, then simply ignore the * and move
            # to the next character in the pattern, but stay on the same character in the other string.
            star_matches_no_one = solve(s1, i - 1, s2, j)

            # if we say that * can match with the current character of the other string, then we match the other
            # string's character by moving to the next character in the other string but staying at the * in the pattern
            # string, because we need to check if * can match with the next character of the other string as well and
            # so on.
            star_matches_with_current_char_in_other_string = solve(s1, i, s2, j - 1)

            # take a logical OR of both the cases and return. Basically, return a true if either of the ways the string
            # match.
            return star_matches_no_one or star_matches_with_current_char_in_other_string
        return False

    def match_strings(s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        # start checking for pattern match from the last indices of both the strings.
        return solve(s1, n1 - 1, s2, n2 - 1)

    print(match_strings("aa", "a"))
    print(match_strings("cb", "?a"))
    print(match_strings("*", "aa"))
    print(match_strings("ge?ks*", "geeksforgeeks"))
    print(match_strings("ge*ks", "geeks"))
    print(match_strings("ba*a?", "baaabab"))
    print(match_strings("a*ab", "baaabab"))


def memoized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 + n2 + {n1 * n2})
    """

    def solve(s1: str, i: int, s2: str, j: int, dp) -> bool:
        # if both the strings become empty at the same time, then strings have matched, return True.
        if i < 0 and j < 0:
            return True

        # if pattern string has exhausted, but not the other string, return False
        if i < 0 and j >= 0:
            return False

        # if pattern string is present, but the other string has exhausted...
        if i >= 0 and j < 0:
            # check for all the leftover characters in the pattern string
            for k in range(i, -1, -1):
                # if any character in the pattern is not a "*", return False, because if all of them are *s,
                # then only we can match the pattern string with an empty string.
                if s1[k] != "*":
                    return False
            return True

        if dp[i][j] is not None:
            return dp[i][j]

        # if characters from both strings match or the character in the pattern string is a "?", then there is a match,
        # call the recursion for next characters in both the strings.
        if s1[i] == s2[j] or s1[i] == "?":
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp)
        elif s1[i] == "*":
            # if the current character from the pattern string is a "*", then the * can match with either 0 characters
            # from the other string, or a number of continuous characters from the other string.

            # if we say that * does not match with any character in the other string, then simply ignore the * and move
            # to the next character in the pattern, but stay on the same character in the other string.
            star_matches_no_one = solve(s1, i - 1, s2, j, dp)

            # if we say that * can match with the current character of the other string, then we match the other
            # string's character by moving to the next character in the other string but staying at the * in the pattern
            # string, because we need to check if * can match with the next character of the other string as well and
            # so on.
            star_matches_with_current_char_in_other_string = solve(s1, i, s2, j - 1, dp)

            # take a logical OR of both the cases and return. Basically, return a true if either of the ways the string
            # match.
            dp[i][j] = star_matches_no_one or star_matches_with_current_char_in_other_string
        else:
            dp[i][j] = False
        return dp[i][j]

    def match_strings(s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: None for j in range(n2)} for i in range(n1)}
        # start checking for pattern match from the last indices of both the strings.
        return solve(s1, n1 - 1, s2, n2 - 1, dp)

    print(match_strings("aa", "a"))
    print(match_strings("cb", "?a"))
    print(match_strings("*", "aa"))
    print(match_strings("ge?ks*", "geeksforgeeks"))
    print(match_strings("ge*ks", "geeks"))
    print(match_strings("ba*a?", "baaabab"))
    print(match_strings("a*ab", "baaabab"))


recursive()
print()
memoized()