class Solution:
    @staticmethod
    def get_longest_substring(string, k):
        # edge case
        if k <= 0:
            return

        # define window variables
        n = len(string)
        left = right = 0

        # define tracking variables
        d = {i: 0 for i in string}

        # define result variables
        longest_length = -1e6
        start_index = -1

        # while there is ground to cover...
        while right < n:
            # increment the count of right indexed character
            d[string[right]] += 1

            # if the distinct character count breaches the k-limit, shrink just one unit from left.
            if sum(v > 0 for v in d.values()) > k:
                d[string[left]] -= 1
                left += 1
            else:
                # else, update the result variables
                if longest_length < right - left + 1:
                    longest_length = right - left + 1
                    start_index = left

            # increment the right index.
            right += 1

        # return the substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest_substring("aaabbccd", 2))
print(Solution.get_longest_substring("abbbbbbc", 2))
print(Solution.get_longest_substring("abcddefg", 3))
print(Solution.get_longest_substring("aaaaaaaa", 3))
print(Solution.get_longest_substring("abcefg", 1))
print(Solution.get_longest_substring("aabbcc", 1))
print(Solution.get_longest_substring("aabbcc", 2))
print(Solution.get_longest_substring("aabbcc", 3))
print(Solution.get_longest_substring("aaabbb", 3))