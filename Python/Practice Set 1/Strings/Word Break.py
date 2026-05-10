def recursive():
    def word_break(string, dictionary):
        return solve(0, string, dictionary, len(string))

    def solve(i, string, dictionary, n):
        # if `i` has reached end, then it means, 0 to i part is present in the dictionary and nothing is left
        # after it. So, return True.
        if i == n:
            return True

        temp = ""
        for j in range(i, n):
            temp += string[j]
            if temp in dictionary and solve(j + 1, string, dictionary, n):
                return True
        return False

    print(word_break("ilike", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("ilikesamsung", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(word_break("storybook", ["story", "book"]))
    print(word_break("monkeyandonkey", ["monkey", "donkey", "and"]))
    print(word_break("applepenapple", ["apple", "pen"]))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(2n).
    """
    def word_break(string, dictionary):
        n = len(string)
        dp = {i: None for i in range(n + 1)}
        return solve(0, string, dictionary, n, dp)

    def solve(i, string, dictionary, n, dp):
        # if `i` has reached end, then it means, 0 to i part is present in the dictionary and nothing is left
        # after it. So, return True.
        if i == n:
            return True
        if dp[i] is not None:
            return dp[i]
        temp = ""
        for j in range(i, n):
            temp += string[j]
            if temp in dictionary and solve(j + 1, string, dictionary, n, dp):
                dp[i] = True
                return True
        dp[i] = False
        return False

    print(word_break("ilike", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("ilikesamsung", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(word_break("storybook", ["story", "book"]))
    print(word_break("monkeyandonkey", ["monkey", "donkey", "and"]))
    print(word_break("applepenapple", ["apple", "pen"]))


recursive()
print()
memoized()
print()
