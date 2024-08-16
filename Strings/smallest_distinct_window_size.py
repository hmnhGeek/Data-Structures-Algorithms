# Problem Link - https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1

def get_distinct_characters(string: str) -> dict:
    # This function, in O(n) time, returns the unique characters in a string with count set to 0.
    # In worst case, space utilized will be O(26) = O(1).
    result = dict()

    for character in string:
        if character not in result:
            result[character] = 0

    return result


def at_least_one_character_not_found_yet(character_set: dict) -> bool:
    # In worst case, O(26) time = O(1) time.
    return any(v == 0 for v in character_set.values())


def get_smallest_distinct_window(string: str) -> int:
    # Time complexity is O(N) and space is O(1).

    # O(n) to compute this with O(1) space.
    character_set = get_distinct_characters(string)

    # initialize a sliding window
    low, high, n = 0, 0, len(string)

    # set the minimum length of the window to be infinite
    min_size_of_window = float('inf')

    # until the window's right boundary does not go out of bounds (on worst case runs 2N times)
    while high < n:
        # in O(1) time, check if there is still some character which has not been found yet. If yes,
        # then continue expanding on the right and also increase the count of the high-indexed character.
        if at_least_one_character_not_found_yet(character_set):
            character_set[string[high]] += 1
            high += 1
        else:
            # as soon as we see that all the characters have been found at least once, we update the min window size,
            # and now, we start decreasing the window length from left side. This way, we will shrink the window from
            # left side or expand from the right side until we get the least possible size.
            min_size_of_window = min(min_size_of_window, high - low)
            character_set[string[low]] -= 1
            low += 1

    # However, there's an edge case. Consider this string: geeksgeeksfor. In one complete iteration, high will become
    # 13 and low is still at 0. If the following code is not there, then the answer would have been set to 13 which is
    # wrong. This is happening because there is at least one character which is found only once and that too at the very
    # end, and so, to get all the characters for the first time, the high pointer moves out. However, we have not yet
    # shrunk from the left side. Because of that, we have to additionally check for left boundary. After doing this,
    # we don't need to expand from right anymore, as `high` has already crossed the right boundary.
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