class Solution:
    @staticmethod
    def get_num_substrings(string):
        # define tracking variables
        d = {"a": 0, "b": 0, "c": 0}

        # define window variables
        left = right = 0
        n = len(string)

        # define result variable
        count = 0

        # while there is ground to cover.
        while right < n:
            # increment right index value.
            d[string[right]] += 1

            # if all the characters are present in the window
            while all(v > 0 for v in d.values()):
                # add to the count
                count += (n - right)

                # shrink from left
                d[string[left]] -= 1
                left += 1

            # increment right index
            right += 1

        # return the count.
        return count


print(Solution.get_num_substrings("bbacba"))
print(Solution.get_num_substrings("abcabc"))
print(Solution.get_num_substrings("aaacb"))
print(Solution.get_num_substrings("abc"))
print(Solution.get_num_substrings("aabbabab"))
