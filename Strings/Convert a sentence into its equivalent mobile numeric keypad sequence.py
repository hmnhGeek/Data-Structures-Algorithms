class Solution:
    _keypad = {
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PQRS",
        8: "TUV",
        9: "WXYZ",
        0: " "
    }

    @staticmethod
    def get_numeric_representation(string):
        result = ""
        cache = {}
        for i in string:
            if i in cache:
                result += cache[i]
                continue
            for key in Solution._keypad:
                if i in Solution._keypad[key]:
                    j = 0
                    sequence = Solution._keypad[key]
                    key_seq = ""
                    while j < len(sequence) and sequence[j] != i:
                        result += str(key)
                        key_seq += str(key)
                        cache[sequence[j]] = key_seq
                        j += 1
                    result += str(key)
                    key_seq += str(key)
                    cache[i] = key_seq
                    break
        return result


print(Solution.get_numeric_representation("GEEKSFORGEEKS"))
print(Solution.get_numeric_representation("HELLO WORLD"))
print(Solution.get_numeric_representation("GFG"))
print(Solution.get_numeric_representation("HEY U"))
print(Solution.get_numeric_representation("CODINGNINJAS"))
print(Solution.get_numeric_representation("PREPINSTA"))
