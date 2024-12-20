class Solution:
    @staticmethod
    def solve(string):
        n = len(string)
        left = right = 0
        count = 0
        d = {"a": 0, "b": 0, "c": 0}
        while right < n:
            d[string[right]] += 1
            while sum(1 for v in d.values() if v != 0) == 3:
                count += (n - right)
                d[string[left]] -= 1
                left += 1
            right += 1
        return count


print(Solution.solve("bbacba"))
print(Solution.solve("abcabc"))
print(Solution.solve("aaacb"))
print(Solution.solve("abc"))
print(Solution.solve("aabbabab"))
