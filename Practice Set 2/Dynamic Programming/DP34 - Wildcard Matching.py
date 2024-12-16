def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """
    def solve(s1, i, s2, j):
        if i == 0 and j == 0:
            return True
        if i == 0 and j > 0:
            return False
        if i > 0 and j == 0:
            match_possible = True
            for k in range(i + 1):
                if s1[k - 1] != "*":
                    match_possible = False
                    break
            return match_possible
        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            return solve(s1, i - 1, s2, j - 1)
        elif s1[i - 1] == "*":
            return solve(s1, i - 1, s2, j) or solve(s1, i, s2, j - 1)
        else:
            return False

    def match(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    print(match("ab*cd", "abdefcd"))
    print(match("ab?d", "abcc"))
    print(match("?ay", "ray"))
    print(match("ba*a?", "baaabab"))
    print(match("*", "abc"))
    print(match("a*ab", "baaabab"))
    print(match("a?c*", "abcde"))
    print(match("?a", "cb"))


recursive()