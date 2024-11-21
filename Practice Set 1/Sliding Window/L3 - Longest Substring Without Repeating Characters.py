# Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


class Solution:
    @staticmethod
    def get_longest_length(string: str):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        # initialize left and right pointers and the longest length variable.
        left, right = 0, 0
        longest_length = 0

        # initialize a dictionary to mark the count of each character.
        d = {i: 0 for i in string}

        # store the start index in case you want to print the substring as well.
        start_index = 0
        n = len(string)

        # while there is ground to cover.
        while right < n:
            # first simply increment the count of `right` indexed character.
            d[string[right]] += 1

            # now, if there is any character which has >= 2 frequency, then shrink one unit from left.
            # Do not worry if it will reduce that >= 2 frequency or not, just reduce one character from left. Basically,
            # here, we are trying to maintain the longest length that we have obtained till now. In case, there are
            # still characters present in d having >= 2 frequency, they shall be taken care of in the next iterations.
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1
            else:
                # else, if all the characters have either a 0 frequency or 1 frequency, update the longest length.
                # update the start index with left pointer as well.
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # finally, increment right pointer in both the cases. Why in the first case? Because we have to maintain
            # the longest window size. We have shrunk left side, but to maintain the same longest length of the window,
            # we have to expand by one unit on right. The other reason is that we have already incremented the count of
            # d[string[right]] by 1 at the first step.
            right += 1

        # return longest length and that substring.
        return longest_length, string[start_index:start_index+longest_length]


print(Solution.get_longest_length("cadbzabcd"))
print(Solution.get_longest_length("abcabcbb"))
print(Solution.get_longest_length("bbbbb"))
print(Solution.get_longest_length("pwwkew"))