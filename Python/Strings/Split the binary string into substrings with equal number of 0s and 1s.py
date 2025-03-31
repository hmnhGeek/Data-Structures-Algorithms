# Problem link - https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/
# Use first solution from problem link. Don't refer to any video.


def split_binary_string(string: str) -> int:
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    count0, count1 = 0, 0
    n = len(string)
    count_substrings = 0

    # iterate on the string in O(n) time and at each iteration check if count of 0s and 1s is same or not. If same,
    # increment the substring count, else continue.
    for i in range(n):
        if string[i] == '0':
            count0 += 1
        if string[i] == '1':
            count1 += 1
        if count0 == count1:
            count_substrings += 1

    # if at the end the counts don't match, the string cannot have such substrings. Return -1.
    if count0 != count1:
        return -1
    # else return substring count.
    return count_substrings


print(split_binary_string("0100110101"))
print(split_binary_string("0111100010"))
print(split_binary_string("0000000000"))