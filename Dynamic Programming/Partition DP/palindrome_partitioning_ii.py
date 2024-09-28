def recursive():
    def solve(string, i, n):
        if i == n:
            return 0
        temp = ""
        min_partitions = float('inf')
        for index in range(i, n):
            temp += string[index]
            if temp == temp[-1:-len(temp)-1:-1]:
                cost = 1 + solve(string, index + 1, n)
                min_partitions = min(min_partitions, cost)
        return min_partitions

    def palindrome_partitioning(string):
        n = len(string)
        return solve(string, 0, n) - 1

    print(palindrome_partitioning("aaccb"))
    print(palindrome_partitioning("ababa"))
    print(palindrome_partitioning("aababa"))

recursive()