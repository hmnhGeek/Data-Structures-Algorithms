# Problem link - https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    @staticmethod
    def lcp(arr):
        # Time complexity is O(min(arr) * n) and space complexity is O(1).
        smallest_string = min(arr, key=len)
        ans = ""
        for i in range(len(smallest_string)):
            for item in arr:
                if item[i] != smallest_string[i]:
                    return ans
            ans += smallest_string[i]
        return ans


print(Solution.lcp(["flower", "flow", "flight"]))
print(Solution.lcp(["dog", "racecar", "car"]))
