class Solution:
    @staticmethod
    def get_lps(pattern):
        m = len(pattern)
        lps = [None] * m
        lps[0] = 0
        i = 1
        length = 0
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length - 1 > 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps