# Problem link - https://leetcode.com/problems/palindrome-partitioning-ii/description/
# Solution - https://www.youtube.com/watch?v=_H8V5hJUGd0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=54


def is_palindrome(string, i, j):
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(string, i, n):
        # if the partition pointer has reached end, there can be no further partitions, return 0.
        if i == n:
            return 0

        # hold a min_partitions.
        min_partitions = float('inf')

        # loop from `i` till `n` and try to see if partition can be done at the given index.
        for index in range(i, n):
            # if the temp string formed till now is a palindrome, then add `1` to the answer to create
            # a partition and recursively solve for the right part.
            if is_palindrome(string, i, index):
                cost = 1 + solve(string, index + 1, n)
                # also update the min_partitions
                min_partitions = min(min_partitions, cost)

        # finally return the answer
        return min_partitions

    def palindrome_partitioning(string):
        n = len(string)
        return solve(string, 0, n) - 1

    print(palindrome_partitioning("aaccb"))
    print(palindrome_partitioning("ababa"))
    print(palindrome_partitioning("aababa"))
    print(palindrome_partitioning("aab"))
    print(palindrome_partitioning("a"))
    print(palindrome_partitioning("ab"))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n + n).
    """
    def solve(string, i, n, dp):
        # if the partition pointer has reached end, there can be no further partitions, return 0.
        if i == n:
            return 0

        if dp[i] is not None:
            return dp[i]

        # store min_partitions
        min_partitions = float('inf')

        # loop from `i` till `n` and try to see if partition can be done at the given index.
        for index in range(i, n):
            # if the temp string formed till now is a palindrome, then add `1` to the answer to create
            # a partition and recursively solve for the right part.
            if is_palindrome(string, i, index):
                cost = 1 + solve(string, index + 1, n, dp)
                # also update the min_partitions
                min_partitions = min(min_partitions, cost)

        # finally return the answer
        dp[i] = min_partitions
        return min_partitions

    def palindrome_partitioning(string):
        n = len(string)
        dp = {i: None for i in range(n)}
        return solve(string, 0, n, dp) - 1

    print(palindrome_partitioning("aaccb"))
    print(palindrome_partitioning("ababa"))
    print(palindrome_partitioning("aababa"))
    print(palindrome_partitioning("aab"))
    print(palindrome_partitioning("a"))
    print(palindrome_partitioning("ab"))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def palindrome_partitioning(string):
        n = len(string)
        dp = {i: float('inf') for i in range(n + 1)}
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            # store min_partitions
            min_partitions = float('inf')

            # loop from `i` till `n` and try to see if partition can be done at the given index.
            for index in range(i, n):
                # if the temp string formed till now is a palindrome, then add `1` to the answer to create
                # a partition and recursively solve for the right part.
                if is_palindrome(string, i, index):
                    cost = 1 + dp[index + 1]
                    # also update the min_partitions
                    min_partitions = min(min_partitions, cost)

            # finally return the answer
            dp[i] = min_partitions

        return dp[0] - 1

    print(palindrome_partitioning("aaccb"))
    print(palindrome_partitioning("ababa"))
    print(palindrome_partitioning("aababa"))
    print(palindrome_partitioning("aab"))
    print(palindrome_partitioning("a"))
    print(palindrome_partitioning("ab"))


print("Recursion Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()
