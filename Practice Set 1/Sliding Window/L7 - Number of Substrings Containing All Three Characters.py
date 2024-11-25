class Solution:
    @staticmethod
    def contains_all_3(string):
        n = len(string)
        left, right = 0, 0
        d = {"a": 0, "b": 0, "c": 0}
        count = 0
        while right < n:
            d[string[right]] += 1
            while not any(v == 0 for v in d.values()):
                count += (n - right)
                d[string[left]] -= 1
                left += 1
            right += 1
        return count


print(Solution.contains_all_3("bbacba"))
print(Solution.contains_all_3("abcabc"))
print(Solution.contains_all_3("aaacb"))
print(Solution.contains_all_3("abc"))