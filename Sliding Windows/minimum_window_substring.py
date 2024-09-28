from collections import Counter


def window_satisfied(temp_map, required_map):
    for i in temp_map:
        if temp_map[i] < required_map[i]:
            return False
    return True


def minimum_window_substring(string, sub):
    required_map = dict(Counter(sub))
    temp_map = {i: 0 for i in required_map}
    i, j = 0, 0
    n = len(string)
    result = ""

    while j < n:
        if string[j] in temp_map:
            temp_map[string[j]] += 1
            while window_satisfied(temp_map, required_map):
                result = string[i:j+1]
                if string[i] in temp_map:
                    temp_map[string[i]] -= 1
                i += 1
        j += 1

    return result


print(minimum_window_substring("ddaaabbca", "abbc"))
print(minimum_window_substring("ADOBECODEBANC", "ABC"))
print(minimum_window_substring("a", "a"))
print(minimum_window_substring("a", "aa"))
print(minimum_window_substring("timetopractice", "toc"))
print(minimum_window_substring("zoomlazapzo", "oza"))