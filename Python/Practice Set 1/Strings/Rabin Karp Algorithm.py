# Problem link - https://www.geeksforgeeks.org/dsa/rabin-karp-algorithm-for-pattern-searching/


class Solution:
    @staticmethod
    def _compute_hash(string):
        hash, base, pow, prime = 0, 26, 0, 101
        for i in range(len(string) - 1, -1, -1):
            hash += (ord(string[i]) * (base ** pow)) % prime
            pow += 1
        return hash

    @staticmethod
    def rabin_karp(text, pattern):
        """
            Time complexity is O(nm) and space complexity is O(m).
        """
        n = len(text)
        m = len(pattern)
        matches = []
        pattern_hash = Solution._compute_hash(pattern)
        for i in range(n - m + 1):
            current_window = text[i:i+m]
            window_hash = Solution._compute_hash(current_window)
            if window_hash == pattern_hash:
                if current_window == pattern:
                    matches.append(i)
        return matches


print(Solution.rabin_karp("ababdabacdababcabab", "ababcabab"))
print(Solution.rabin_karp("geeksforgeeks", "geek"))
print(Solution.rabin_karp("aabaacaadaabaaba", "aaba"))
print(Solution.rabin_karp("ababcabcababc", "abc"))
print(Solution.rabin_karp("hello", "ll"))
