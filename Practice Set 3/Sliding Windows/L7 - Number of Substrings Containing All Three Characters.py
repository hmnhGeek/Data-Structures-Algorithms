class Solution:
    @staticmethod
    def get_substrings(string):
        n = len(string)
        left = right = 0
        d = {"a": 0, "b": 0, "c": 0}
        count = 0
        while right < n:
            d[string[right]] += 1
            while sum(1 for v in d.values() if v > 0) == 3:
                count += (n - right)
                d[string[left]] -= 1
                left += 1
            right += 1
        return count


print(Solution.get_substrings("bbacba"))
print(Solution.get_substrings("abcabc"))
print(Solution.get_substrings("aaacb"))
print(Solution.get_substrings("abc"))