class Solution:
    @staticmethod
    def get_longest(string, k):
        left = right = 0
        d = {i: 0 for i in string}
        n = len(string)
        longest_length = 0
        start_index = -1
        while right < n:
            d[string[right]] += 1
            if sum(1 for v in d.values() if v > 0) > k:
                d[string[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v > 0) <= k:
                if longest_length <= right - left + 1:
                    longest_length = right - left + 1
                    start_index = left
            right += 1
        while left < n:
            if sum(1 for v in d.values() if v > 0) <= k:
                if longest_length <= n - left:
                    longest_length = n - left
                    start_index = left
            d[string[left]] -= 1
            left += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest("aaabbccd", 2))
print(Solution.get_longest("abbbbbbc", 2))
print(Solution.get_longest("abcddefg", 3))
print(Solution.get_longest("aaaaaaaa", 3))
print(Solution.get_longest("abcefg", 1))