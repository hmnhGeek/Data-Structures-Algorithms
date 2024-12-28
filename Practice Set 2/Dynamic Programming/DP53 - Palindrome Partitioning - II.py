def is_palindrome(string):
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(string, i, n):
        if i == n:
            return 0
        min_cost = 1e6
        temp = ""
        for j in range(i, n):
            temp += string[j]
            if is_palindrome(temp):
                cost = 1 + solve(string, j + 1, n)
                min_cost = min(min_cost, cost)
        return min_cost

    def get_min_partitions_count(string):
        n = len(string)
        return solve(string, 0, n) - 1

    print(get_min_partitions_count("aaccb"))
    print(get_min_partitions_count("ababa"))
    print(get_min_partitions_count("aababa"))
    print(get_min_partitions_count("aab"))
    print(get_min_partitions_count("a"))
    print(get_min_partitions_count("ab"))
    print(get_min_partitions_count("geek"))
    print(get_min_partitions_count("ababbbabbababa"))
    print(get_min_partitions_count("bababcbadcede"))


def memoized():
    """
        Time complexity is O(n^2 * m) where m is the length of longest temp string and space complexity is O(n * m).
    """

    def solve(string, i, n, dp):
        if i == n:
            return 0
        if dp[i] is not None:
            return dp[i]
        min_cost = 1e6
        temp = ""
        for j in range(i, n):
            temp += string[j]
            if is_palindrome(temp):
                cost = 1 + solve(string, j + 1, n, dp)
                min_cost = min(min_cost, cost)
        dp[i] = min_cost
        return dp[i]

    def get_min_partitions_count(string):
        n = len(string)
        dp = {i: None for i in range(n + 1)}
        return solve(string, 0, n, dp) - 1

    print(get_min_partitions_count("aaccb"))
    print(get_min_partitions_count("ababa"))
    print(get_min_partitions_count("aababa"))
    print(get_min_partitions_count("aab"))
    print(get_min_partitions_count("a"))
    print(get_min_partitions_count("ab"))
    print(get_min_partitions_count("geek"))
    print(get_min_partitions_count("ababbbabbababa"))
    print(get_min_partitions_count("bababcbadcede"))


recursive()
print()
memoized()
