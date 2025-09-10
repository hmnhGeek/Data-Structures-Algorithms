class Solution:
    @staticmethod
    def get_run_length_encoding(string):
        n = len(string)
        i = 0
        result = ""
        while i < n:
            character = string[i]
            j = i
            count = 0
            while j < n and string[j] == character:
                count += 1
                j += 1
            result += f"{count}{character}"
            i = j
        return result


print(Solution.get_run_length_encoding("3322251"))