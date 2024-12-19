class Solution:
    @staticmethod
    def get_longest(arr, k):
        if k < 0:
            return -1

        left = right = 0
        n = len(arr)
        d = {i: 0 for i in arr}
        longest_length = 0
        start_index = -1

        while right < n:
            d[arr[right]] += 1
            if sum(1 for v in d.values() if v != 0) > k:
                d[arr[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v != 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1

        return arr[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest("aaabbccd", 2))
print(Solution.get_longest("abbbbbbc", 2))
print(Solution.get_longest("abcddefg", 3))
print(Solution.get_longest("aaaaaaaa", 3))
print(Solution.get_longest("abcefg", 1))
print(Solution.get_longest("aabbcc", 1))
print(Solution.get_longest("aabbcc", 2))
print(Solution.get_longest("aabbcc", 3))
print(Solution.get_longest("aaabbb", 3))
