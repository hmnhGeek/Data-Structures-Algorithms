from collections import OrderedDict


class Solution:
    @staticmethod
    def choose_and_swap(string):
        string = [i for i in string]
        hash_map = sorted(set(string))
        for i in range(len(string)):
            hash_map.remove(string[i])
            if len(hash_map) == 0:
                return
            character = list(hash_map)[0]
            if ord(character) < ord(string[i]):
                second_character = string[i]
                for j in range(len(string)):
                    if string[j] == character:
                        string[j] = second_character
                    elif string[j] == second_character:
                        string[j] = character
                break
        return "".join(string)


print(Solution.choose_and_swap("ccad"))