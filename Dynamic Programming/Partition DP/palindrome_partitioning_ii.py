def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(string, i, n):
        # if the partition pointer has reached end, there can be no further partitions, return 0.
        if i == n:
            return 0

        # hold a temp string for palindrome checks on the partitioned string.
        temp = ""
        min_partitions = float('inf')

        # loop from `i` till `n` and try to see if partition can be done at the given index.
        for index in range(i, n):
            # store the character at the index.
            temp += string[index]

            # if the temp string formed till now is a palindrome, then add `1` to the answer to create
            # a partition and recursively solve for the right part.
            if temp == temp[-1:-len(temp)-1:-1]:
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
        Time complexity is O(n^2) and space complexity is O(n + n^2).
    """
    def solve(string, i, n, dp):
        # if the partition pointer has reached end, there can be no further partitions, return 0.
        if i == n:
            return 0

        if dp[i] is not None:
            return dp[i]

        # hold a temp string for palindrome checks on the partitioned string.
        temp = ""
        min_partitions = float('inf')

        # loop from `i` till `n` and try to see if partition can be done at the given index.
        for index in range(i, n):
            # store the character at the index.
            temp += string[index]

            # if the temp string formed till now is a palindrome, then add `1` to the answer to create
            # a partition and recursively solve for the right part.
            if temp == temp[-1:-len(temp)-1:-1]:
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


recursive()
print()
memoized()