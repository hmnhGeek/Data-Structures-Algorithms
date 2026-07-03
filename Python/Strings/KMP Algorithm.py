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

    @staticmethod
    def find_pattern(string, pattern):
        n, m = len(string), len(pattern)
        lps = Solution.get_lps(pattern)
        i = j = 0
        results = []
        while i < n:
            if string[i] == pattern[j]:
                i += 1
                j += 1
            if j == m:
                results.append(i - j)
                j = lps[j - 1]
                i += 1
            elif string[i] != pattern[j]:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return results


