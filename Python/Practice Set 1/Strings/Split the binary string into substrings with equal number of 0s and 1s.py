class Solution:
    @staticmethod
    def split_binary_string(string):
        counter = -1 if string[0] == "0" else 1
        i = 1
        last_index = 0
        result = []
        while i < len(string):
            if string[i] == "0":
                counter -= 1
            else:
                counter += 1
            if counter == 0:
                result.append(string[last_index:i+1])
                last_index = i + 1
            i += 1
        return result


print(Solution.split_binary_string("0100110101"))
print(Solution.split_binary_string("0111100010"))
print(Solution.split_binary_string("0000000000"))
