def solve_num_distinct_subsequences(string, i, lookup, j):
    # if at any point there is nothing to left in string to compare, return 0.
    if i < 0:
        return 0

    # if you are at 0th index of lookup string, you must be fixed on it and continuously check
    # for characters in `string` and add up 1 as and when match is completed.
    if j == 0:
        # if the ith index character in string matches with first character of lookup string,
        # add 1, but stay on same `j` index and look for lower indices in string. Basically,
        # here we are trying to find the count of distinct subsequences which start with
        # character lookup[0]. Else, don't add this 1, and simply do the same.
        if string[i] == lookup[0]:
            return 1 + solve_num_distinct_subsequences(string, i - 1, lookup, j)
        else:
            return solve_num_distinct_subsequences(string, i - 1, lookup, j)

    # again, if the characters in both the strings match, then you've two options at this juncture:
    # 1. reduce indices of both and consider getting a match.
    # 2. reduce only `i` and stay at `j`, basically not considering `i` even though it's a match with `j`.
    if string[i] == lookup[j]:
        left = solve_num_distinct_subsequences(string, i - 1, lookup, j - 1)
        right = solve_num_distinct_subsequences(string, i - 1, lookup, j)
        # return the sum of distinct subsequences so obtained.
        return left + right

    # if there is not a match, you have no option but to stay at same `j` but move lower on `i`.
    return solve_num_distinct_subsequences(string, i - 1, lookup, j)


def get_distinct_subsequences(string, lookup):
    n = len(string)
    m = len(lookup)
    return solve_num_distinct_subsequences(string, n - 1, lookup, m - 1)


print(get_distinct_subsequences("brootgroot", "brt"))
print(get_distinct_subsequences("dingdingdingding", "ing"))
print(get_distinct_subsequences("aaaaa", "a"))