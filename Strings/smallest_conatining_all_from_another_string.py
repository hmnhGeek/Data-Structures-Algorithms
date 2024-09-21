def get_freq(string):
    d = {i: 0 for i in string}
    for i in string:
        d[i] += 1
    return d


def get_smallest_window(main_string, substring):
    freq = get_freq(substring)
    min_length = float('inf')
    i, j = 0, 0
    n = len(main_string)
    substring_count_tracker = {i: 0 for i in substring}
    result = ""

    while j < n:
        while all(v != 0 for v in substring_count_tracker.values()):
            window_size = (j - i)
            if min_length > window_size >= len(substring):
                min_length = window_size
                result = main_string[i:j]

            if main_string[i] in freq:
                substring_count_tracker[main_string[i]] -= 1
            i += 1

        if main_string[j] in freq:
            substring_count_tracker[main_string[j]] += 1
        j += 1

    while all(v != 0 for v in substring_count_tracker.values()):
        window_size = (j - i)
        if min_length > window_size >= len(substring):
            min_length = window_size
            result = main_string[i:j]

        if main_string[i] in freq:
            substring_count_tracker[main_string[i]] -= 1
        i += 1
    return result


print(get_smallest_window("timetopractice", "toc"))
print(get_smallest_window("zoomlazapzo", "oza"))
print(get_smallest_window("ADOBECODEBANC", "ABC"))
print(get_smallest_window("ABBXC", "BXC"))
print(get_smallest_window("ABCKCPCPAAC", "CCP"))