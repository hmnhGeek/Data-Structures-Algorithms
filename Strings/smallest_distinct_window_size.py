# Problem Link - https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1

def get_distinct_characters(string: str) -> dict:
    result = dict()

    for character in string:
        if character not in result:
            result[character] = 0

    return result


def at_least_one_character_not_found_yet(character_set: dict) -> bool:
    return any(v == 0 for v in character_set.values())


def get_smallest_distinct_window(string: str) -> int:
    character_set = get_distinct_characters(string)
    low, high, n = 0, 0, len(string)
    min_size_of_window = float('inf')

    while high < n:
        if at_least_one_character_not_found_yet(character_set):
            character_set[string[high]] += 1
            high += 1
        else:
            min_size_of_window = min(min_size_of_window, high - low)
            character_set[string[low]] -= 1
            low += 1

    while not at_least_one_character_not_found_yet(character_set):
        min_size_of_window = min(min_size_of_window, high - low)
        character_set[string[low]] -= 1
        low += 1

    return min_size_of_window if min_size_of_window != float('inf') else 0


print(get_smallest_distinct_window("geeksgeeksfor"))
print(get_smallest_distinct_window("aaab"))
print(get_smallest_distinct_window("aabbbcbbac"))
print(get_smallest_distinct_window("aabcbcdbca"))
print(get_smallest_distinct_window("mississippi"))