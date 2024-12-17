# Problem link - https://leetcode.com/problems/minimum-window-substring/description/
# Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


from collections import Counter


class Solution:
    @staticmethod
    def _valid_config(d, req):
        """
            Time complexity is O(26) and space complexity is O(1).
        """
        # if any character in d has less count than that in req, return False.
        for i in req:
            if d[i] < req[i]:
                return False
        # else return true.
        return True

    @staticmethod
    def min_window_substring(string, required):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """

        # define window variables
        left = right = 0
        n = len(string)

        # define result variables
        shortest_length = 1e6
        start_index = -1

        # define tracking dictionaries
        d = {i: 0 for i in string}
        req = dict(Counter(required))

        # while there is ground to cover
        while right < n:
            # increment the count of right indexed character
            d[string[right]] += 1

            # if all characters of required string are in d, shrink continuously from left and update min length
            while Solution._valid_config(d, req):
                if shortest_length > right - left + 1:
                    shortest_length = right - left + 1
                    start_index = left
                d[string[left]] -= 1
                left += 1
            # increment right index
            right += 1

        # while right is out but still the configuration is valid, continue the shrink process from left and update the
        # variables.
        while Solution._valid_config(d, req):
            if shortest_length > right - left + 1:
                shortest_length = right - left + 1
                start_index = left
            d[string[left]] -= 1
            left += 1

        # return the shortest string.
        return string[start_index:start_index+shortest_length] if start_index != -1 else ""


print(Solution.min_window_substring("ddaaabbca", "abc"))
print(Solution.min_window_substring("ADOBECODEBANC", "ABC"))
print(Solution.min_window_substring("a", "a"))
print(Solution.min_window_substring("a", "aa"))
print(Solution.min_window_substring("timetopractice", "toc"))
print(Solution.min_window_substring("zoomlazapzo", "oza"))
print(Solution.min_window_substring("ABBXC", "BXC"))
