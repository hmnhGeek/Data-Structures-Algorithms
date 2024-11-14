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


recursive()