class Solution:
    @staticmethod
    def get_num_substrings(string):
        d = {"a": 0, "b": 0, "c": 0}
        left = right = 0
        n = len(string)
        count = 0
        while right < n:
            d[string[right]] += 1
            while all(v > 0 for v in d.values()):
                count += (n - right)
                d[string[left]] -= 1
                left += 1
            right += 1
        return count


print(Solution.get_num_substrings("bbacba"))
print(Solution.get_num_substrings("abcabc"))
print(Solution.get_num_substrings("aaacb"))
print(Solution.get_num_substrings("abc"))
print(Solution.get_num_substrings("aabbabab"))
