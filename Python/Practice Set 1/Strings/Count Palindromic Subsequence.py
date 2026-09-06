def recursive():
    def count(string):
        n = len(string)
        return solve(string, 0, n - 1)

    def solve(string, i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if string[i] == string[j]:
            return 1 + solve(string, i + 1, j) + solve(string, i, j - 1)
        else:
            return solve(string, i + 1, j) + solve(string, i, j - 1) - solve(string, i + 1, j - 1)

    print(count("abcd"))
    print(count("aab"))
    print(count("geeksforgeeks"))
    print(count("103301"))
    print(count("bccb"))


recursive()
print()