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
            if temp == temp[-1:-len(temp)-1:-1]:
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


recursive()