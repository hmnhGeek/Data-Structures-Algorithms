class Solution:
    @staticmethod
    def _get_seq(s: str):
        i = 1
        character = s[i - 1]
        count = 1
        n = len(s)
        result = ""
        while i < n:
            if s[i] == character:
                i += 1
                count += 1
            else:
                result += f"{count}{character}"
                count = 0
                character = s[i]
        return result + f"{count}{character}"

    @staticmethod
    def count_and_say(n):
        i = 0
        start = "1"
        while i != n - 1:
            start = Solution._get_seq(start)
            i += 1
        return start


print(Solution.count_and_say(4))
print(Solution.count_and_say(1))
print(Solution.count_and_say(3))
print(Solution.count_and_say(5))
print(Solution.count_and_say(6))
