class Solution:
    @staticmethod
    def get_longest_substring(string):
        result = ""
        length = 0

        for i in range(len(string)):
            l, r = i, i
            while 0 <= l < len(string) and 0 <= r < len(string) and string[l] == string[r]:
                if length < r - l + 1:
                    length = r - l + 1
                    result = string[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while 0 <= l < len(string) and 0 <= r < len(string) and string[l] == string[r]:
                if length < r - l + 1:
                    length = r - l + 1
                    result = string[l:r+1]
                l -= 1
                r += 1

        return result


print(Solution.get_longest_substring("forgeeksskeegfor"))