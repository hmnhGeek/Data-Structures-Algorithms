# Problem link - https://www.naukri.com/code360/problems/palindrome-partitioning_873266?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=_H8V5hJUGd0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=54


def is_palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    n = len(string)
    i, j = 0, n - 1
    while i <= j:
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
        for j in range(i, n):
            substring = string[i:j + 1]
            if is_palindrome(substring):
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
        Time complexity is O(n^2 * m) and space complexity is O(n + n*m).
    """

    def solve(string, i, n, dp):
        if i == n:
            return 0
        if dp[i] is not None:
            return dp[i]
        min_cost = 1e6
        for j in range(i, n):
            substring = string[i:j + 1]
            if is_palindrome(substring):
                cost = 1 + solve(string, j + 1, n, dp)
                min_cost = min(min_cost, cost)
        dp[i] = min_cost
        return dp[i]

    def get_min_partitions_count(string):
        n = len(string)
        dp = {i: None for i in range(n)}
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


def tabulation():
    """
        Time complexity is O(n^2 * m) and space complexity is O(n*m).
    """
    def get_min_partitions_count(string):
        n = len(string)
        dp = {i: 1e6 for i in range(n + 1)}
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            min_cost = 1e6
            for j in range(i, n):
                substring = string[i:j + 1]
                if is_palindrome(substring):
                    cost = 1 + dp[j + 1]
                    min_cost = min(min_cost, cost)
            dp[i] = min_cost
        return dp[0] - 1

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
print()
tabulation()
