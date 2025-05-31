class Solution:
    @staticmethod
    def solve(string, k):
        n = len(string)
        left = right = 0
        d = {'a': 0, 'b': 0, 'c': 0}
        count = 0
        while right < n:
            d[string[right]] += 1
            while sum(1 for v in d.values() if v > 0) > k:
                d[string[left]] -= 1
                left += 1
            else:
                count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def get_num_substrings(string):
        return Solution.solve(string, 3) - Solution.solve(string, 2)


print(Solution.get_num_substrings("bbacba"))
print(Solution.get_num_substrings("abcabc"))
print(Solution.get_num_substrings("aaacb"))
print(Solution.get_num_substrings("abc"))
print(Solution.get_num_substrings("aabbabab"))
