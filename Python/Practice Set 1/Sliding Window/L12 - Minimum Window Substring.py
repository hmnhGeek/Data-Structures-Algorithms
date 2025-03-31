# Problem link - https://leetcode.com/problems/minimum-window-substring/description/
# Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


from collections import Counter


class Solution:
    @staticmethod
    def _window_is_valid(required, given):
        """
            This will take O(26) time.
        """

        # iterate in required dictionary and check if given dictionary has enough elements from required dictionary.
        for i in required:
            if given[i] < required[i]:
                return False
        return True

    @staticmethod
    def minimum_window(string: str, t: str) -> str:
        """
            Overall time complexity is O(26n) and space complexity is O(26).
        """

        # create given frequency map from `t`.
        t_counter = dict(Counter(t))

        # create a tracker dictionary. This will take O(26) space.
        tracker = {i: 0 for i in string}

        # define window variables.
        left = right = 0
        n = len(string)
        min_length = 1e6
        start_index = 0

        # while there is ground to cover. This will take O(n*26) time.
        while right < n:
            # increment the count of `right` indexed tracker.
            tracker[string[right]] += 1

            # while we have sufficient count, update the length continuously.
            while Solution._window_is_valid(t_counter, tracker):
                # update the min length and the start index.
                min_length = min(min_length, right - left + 1)
                start_index = left
                # decrement from left so that we can achieve even shorter window length.
                tracker[string[left]] -= 1
                left += 1

            # increment right.
            right += 1

        # after right >= n, it could be possible that we can achieve shorter window length, hence decrement from left.
        # This will take O(n * 26) time.
        while Solution._window_is_valid(t_counter, tracker):
            min_length = min(min_length, right - left + 1)
            start_index = left
            tracker[string[left]] -= 1
            left += 1

        # return the resultant string.
        return string[start_index:start_index+min_length] if min_length != 1e6 else ""


print(Solution.minimum_window("ddaaabbca", "abc"))
print(Solution.minimum_window("timetopractice", "toc"))
print(Solution.minimum_window("zoomlazapzo", "oza"))
print(Solution.minimum_window("ADOBECODEBANC", "ABC"))
print(Solution.minimum_window("a", "a"))
print(Solution.minimum_window("a", "aa"))
print(Solution.minimum_window("ABBXC", "BXC"))
