def recursive():
    def solve(string, i, j):
        if i >= j:
            return True
        if string[i] == string[j]:
            return solve(string, i + 1, j - 1)
        else:
            return False

    def get_longest_palindromic_substring(string: str):
        start = 0
        length = 0
        n = len(string)
        for i in range(n):
            for j in range(i, n):
                if solve(string, i, j) and j - i + 1 > length:
                    start = i
                    length = j - i + 1
        return string[start:start+length]


    print(get_longest_palindromic_substring("aaaabbaa"))


recursive()