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
    def word_break(string, dictionary):
        n = len(string)
        dp = {i: None for i in range(2*n + 1)}
        return solve(0, string, dictionary, n, dp)

    def solve(i, string, dictionary, n, dp):
        # if `i` has reached end, then it means, 0 to i part is present in the dictionary and nothing is left
        # after it. So, return True.
        if i == n:
            return True

        if dp[i] is not None:
            return dp[i]

        # before moving to partitioning, check if the whole string is present in the dictionary or not.
        if string in dictionary:
            return True

        # now, partition by length
        for length in range(1, n + 1):
            # get the substring and check for the second part.
            substring = string[i:i+length]
            if substring in dictionary and solve(i + length, string, dictionary, n, dp):
                dp[i] = True

        # return false if second part is not found in the dictionary.
        dp[i] = False
        return dp[i]

    print(word_break("ilike", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("ilikesamsung", ["i", "like", "sam", "sung", "samsung", "mobile"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(word_break("storybook", ["story", "book"]))
    print(word_break("monkeyandonkey", ["monkey", "donkey", "and"]))
    print(word_break("applepenapple", ["apple", "pen"]))


recursive()
print()
# memoized()
print()
