class Solution:
    @staticmethod
    def solve(string, k):
        # window variables
        n = len(string)
        left = right = 0

        # tracking variable
        d = {'a': 0, 'b': 0, 'c': 0}

        # result variable
        count = 0

        # while there is ground to cover...
        while right < n:
            # increment the right indexed count
            d[string[right]] += 1

            # while the number of characters have breached `k` value...
            while sum(1 for v in d.values() if v > 0) > k:
                # shrink continuously from left.
                d[string[left]] -= 1
                left += 1
            else:
                # else increment the count.
                count += (right - left + 1)

            # increment the right index
            right += 1

        # return the count.
        return count

    @staticmethod
    def get_num_substrings(string):
        return Solution.solve(string, 3) - Solution.solve(string, 2)


print(Solution.get_num_substrings("bbacba"))
print(Solution.get_num_substrings("abcabc"))
print(Solution.get_num_substrings("aaacb"))
print(Solution.get_num_substrings("abc"))
print(Solution.get_num_substrings("aabbabab"))
