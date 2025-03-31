# Problem link - https://www.naukri.com/code360/problems/palindrome-partitioning_873266?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=_H8V5hJUGd0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=54


def is_palindrome(string: str):
    n = len(string)
    i, j = 0, n - 1
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

    def palindrome_partitioning(string: str):
        n = len(string)
        # solve function will return the number of partitions and we need number of cuts
        # return solve - 1.
        return solve(string, 0, n) - 1

    print(palindrome_partitioning("aaccb"))
    print(palindrome_partitioning("ababa"))
    print(palindrome_partitioning("aababa"))
    print(palindrome_partitioning("aab"))
    print(palindrome_partitioning("a"))
    print(palindrome_partitioning("ab"))
    print(palindrome_partitioning("geek"))
    print(palindrome_partitioning("ababbbabbababa"))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n + n).
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

    def palindrome_partitioning(string: str):
        n = len(string)
        dp = {i: None for i in range(n)}
        # solve function will return the number of partitions and we need number of cuts
        # return solve - 1.
        return solve(string, 0, n, dp) - 1

    print(palindrome_partitioning("aaccb"))
    print(palindrome_partitioning("ababa"))
    print(palindrome_partitioning("aababa"))
    print(palindrome_partitioning("aab"))
    print(palindrome_partitioning("a"))
    print(palindrome_partitioning("ab"))
    print(palindrome_partitioning("geek"))
    print(palindrome_partitioning("ababbbabbababa"))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def palindrome_partitioning(string: str):
        n = len(string)
        dp = {i: 1e6 for i in range(n + 1)}
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            min_cost = 1e6
            temp = ""
            for j in range(i, n):
                temp += string[j]
                if is_palindrome(temp):
                    cost = 1 + dp[j + 1]
                    min_cost = min(min_cost, cost)
            dp[i] = min_cost

        # solve function will return the number of partitions and we need number of cuts
        # return solve - 1.
        return dp[0] - 1

    print(palindrome_partitioning("aaccb"))
    print(palindrome_partitioning("ababa"))
    print(palindrome_partitioning("aababa"))
    print(palindrome_partitioning("aab"))
    print(palindrome_partitioning("a"))
    print(palindrome_partitioning("ab"))
    print(palindrome_partitioning("geek"))
    print(palindrome_partitioning("ababbbabbababa"))


recursive()
print()
memoized()
print()
tabulation()
