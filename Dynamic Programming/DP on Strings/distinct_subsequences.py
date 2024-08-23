def solve_num_distinct_subsequences(string, i, lookup, j):
    if i < 0:
        return 0
    if j == 0:
        if string[i] == lookup[0]:
            return 1 + solve_num_distinct_subsequences(string, i - 1, lookup, j)
        else:
            return solve_num_distinct_subsequences(string, i - 1, lookup, j)

    if string[i] == lookup[j]:
        left = solve_num_distinct_subsequences(string, i - 1, lookup, j - 1)
        right = solve_num_distinct_subsequences(string, i - 1, lookup, j)
        return left + right
    return solve_num_distinct_subsequences(string, i - 1, lookup, j)


def get_distinct_subsequences(string, lookup):
    n = len(string)
    m = len(lookup)
    return solve_num_distinct_subsequences(string, n - 1, lookup, m - 1)


print(get_distinct_subsequences("brootgroot", "brt"))
print(get_distinct_subsequences("dingdingdingding", "ing"))
print(get_distinct_subsequences("aaaaa", "a"))