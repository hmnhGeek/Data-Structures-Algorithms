class Solution:
    @staticmethod
    def lcp(strings):
        """
            Time complexity is O(n * m) and space complexity is O(n) where n is the avg length of all the strings and
            there are m strings.
        """

        result = ""

        # assume that you are checking all the string wrt to the 0th string. The 0th string could be or could not be the
        # smallest string.
        for i in range(len(strings[0])):
            # now loop on all the strings.
            for string in strings:
                # if the length of this string <= i, we are out of bounds for this string, no need to check further,
                # return the result. Or, if everything is fine wrt indices but string[i] character does not match with
                # 0th string's ith character, then also return the result.
                if i >= len(string) or string[i] != strings[0][i]:
                    return result

            # finally add the 0th string character into result, as it was a match.
            result += strings[0][i]

        # return the final result.
        return result


print(Solution.lcp(["flower", "flow", "flight"]))
print(Solution.lcp(["dog", "racecar", "car"]))
