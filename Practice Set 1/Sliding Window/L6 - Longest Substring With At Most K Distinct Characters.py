class Solution:
    @staticmethod
    def get_longest_substring(string: str, k: int):
        """
            Overall time complexity is O(26*n) and space is O(26).
        """

        # assume `d` to store all the alphabets of the English dictionary. Thus O(26) space.
        d = {i: 0 for i in string}

        # define window parameters
        left, right = 0, 0
        n = len(string)

        # define result variables.
        longest_length = 0
        start_index = 0

        # while there is ground to cover. This will take O(n) time.
        while right < n:
            # increment the count of `right` indexed character
            d[string[right]] += 1

            # if the distinct characters count from the dictionary is <= k, update the longest length. This check will
            # take O(26) time.
            if sum(1 for value in d.values() if value != 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                # also update the start index in case substring needs to be printed.
                start_index = left
            # if more than k distinct characters have been considered, don't expand beyond longest length sized window,
            # and decrement one character from left.
            else:
                d[string[left]] -= 1
                left += 1
            # increment right because anyway you've added right character in the window as the first thing in this
            # while block.
            right += 1

        # return results.
        return longest_length, string[start_index:start_index+longest_length]


print(Solution.get_longest_substring("aaabbccd", 2))
print(Solution.get_longest_substring("abbbbbbc", 2))
print(Solution.get_longest_substring("abcddefg", 3))
print(Solution.get_longest_substring("aaaaaaaa", 3))
print(Solution.get_longest_substring("abcefg", 1))
print(Solution.get_longest_substring("aabbcc", 1))
print(Solution.get_longest_substring("aabbcc", 2))
print(Solution.get_longest_substring("aabbcc", 3))
print(Solution.get_longest_substring("aaabbb", 3))