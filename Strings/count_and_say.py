class Solution:
    @staticmethod
    def _get_seq(s: str):
        # point the `i` counter to 1.
        i = 1

        # store the previous character, i.e., 0th character.
        previous_character = s[i - 1]

        # store count = 1 for the 0th character.
        count = 1

        # create other useful variables.
        n = len(s)
        result = ""

        # loop in the string.
        while i < n:
            # check if the previous character is same as the current character
            if s[i] == previous_character:
                # if yes, then increase the count of this stored character.
                count += 1
            else:
                # if the current character is not the same as previous character, then
                # update the resultant string with the count of the previous character and
                # the previous character itself.
                # Now, reset the count to 1 for the current character and set the previous
                # character as s[i].
                result += f"{count}{previous_character}"
                count = 1
                previous_character = s[i]

            # finally, move to the next character.
            i += 1

        # at the end, return the result but append the last previous character and its count before returning.
        return result + f"{count}{previous_character}"

    @staticmethod
    def count_and_say(n):
        # start with n = 0 (base case). Here, f(0) = '1'.
        i = 0
        start = "1"

        # now loop till 3 for n = 4 (example), i.e., n - 1.
        while i != n - 1:
            # build from the start sequence.
            start = Solution._get_seq(start)
            i += 1

        # return the final sequence.
        return start


print(Solution.count_and_say(4))
print(Solution.count_and_say(1))
print(Solution.count_and_say(3))
print(Solution.count_and_say(5))
print(Solution.count_and_say(6))
