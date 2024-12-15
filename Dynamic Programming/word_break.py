def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(string, i, dictionary, n):
        # if the whole string is exhausted, it's because the whole string was able to call solve(). Thus all the word
        # breaks must be present in the dictionary. Thus, return True.
        if i == n:
            return True
        # Typical front-partition DP from Striver's playlist.
        temp = ""
        for j in range(i, n):
            temp += string[j]
            # check if current substring is present in dictionary, and if it is, then check for the next partition as
            # well, and if both return true, then we must return True.
            if temp in dictionary and solve(string, j + 1, dictionary, n):
                return True
        # if there was no place where we could return a True, we must be unable to break the string, thus return False.
        return False

    def word_break(string, dictionary):
        n = len(string)
        return solve(string, 0, dictionary, n)

    print(word_break("ilike", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("ilikesamsung", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(word_break("storybook", ["story", "book"]))
    print(word_break("monkeyandonkey", ["monkey", "donkey", "and"]))
    print(word_break("applepenapple", ["apple", "pen"]))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n + n).
    """
    def solve(string, i, dictionary, n, dp):
        # if the whole string is exhausted, it's because the whole string was able to call solve(). Thus all the word
        # breaks must be present in the dictionary. Thus, return True.
        if i == n:
            return True
        if dp[i] is not None:
            return dp[i]
        # Typical front-partition DP from Striver's playlist.
        temp = ""
        for j in range(i, n):
            temp += string[j]
            # check if current substring is present in dictionary, and if it is, then check for the next partition as
            # well, and if both return true, then we must return True.
            if temp in dictionary and solve(string, j + 1, dictionary, n, dp):
                dp[i] = True
                return True
        # if there was no place where we could return a True, we must be unable to break the string, thus return False.
        dp[i] = False
        return False

    def word_break(string, dictionary):
        n = len(string)
        dp = {i: None for i in range(n)}
        return solve(string, 0, dictionary, n, dp)

    print(word_break("ilike", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("ilikesamsung", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(word_break("storybook", ["story", "book"]))
    print(word_break("monkeyandonkey", ["monkey", "donkey", "and"]))
    print(word_break("applepenapple", ["apple", "pen"]))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def word_break(string, dictionary):
        n = len(string)
        dp = {i: False for i in range(n + 1)}
        dp[n] = True
        for i in range(n - 1, -1, -1):
            # Typical front-partition DP from Striver's playlist.
            temp = ""
            for j in range(i, n):
                temp += string[j]
                # check if current substring is present in dictionary, and if it is, then check for the next
                # partition as well, and if both return true, then we must return True.
                if temp in dictionary and dp[j + 1]:
                    dp[i] = True
                    break
        return dp[0]

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
tabulation()