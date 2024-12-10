class Solution:
    @staticmethod
    def longest_all(string):
        n = len(string)
        left = right = 0
        d = {i: 0 for i in string}
        longest_length, start_index = 0, -1
        while right < n:
            d[string[right]] += 1
            while any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1
            if right - left + 1 > longest_length:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_all("cadbzabcd"))
print(Solution.longest_all("abcabcbb"))
print(Solution.longest_all("bbbbb"))
print(Solution.longest_all("pwwkew"))
print(Solution.longest_all("ABCBC"))
print(Solution.longest_all("GEEKSFORGEEKS"))
print(Solution.longest_all("xyxyz"))
