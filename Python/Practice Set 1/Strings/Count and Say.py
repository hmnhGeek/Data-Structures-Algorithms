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

    @staticmethod
    def count_and_say(n):
        if n == 1:
            return "1"
        return Solution.get_run_length_encoding(Solution.count_and_say(n - 1))


print(Solution.count_and_say(4))
print(Solution.count_and_say(1))
print(Solution.count_and_say(3))
print(Solution.count_and_say(5))
