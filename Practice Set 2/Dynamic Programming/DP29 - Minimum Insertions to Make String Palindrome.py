def recursive():
    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    def min_inserts_for_palindrome(s1, s2):
        n = len(s1)
        m = len(s2)
        return solve(s1, n, s2, m)

    print(min_inserts_for_palindrome("abcd", "abzd"))


recursive()