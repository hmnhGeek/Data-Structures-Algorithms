# Problem link - https://www.geeksforgeeks.org/problems/choose-and-swap0531/1
# Solution - https://www.youtube.com/watch?v=NhnsINajZRA


class Solution:
    @staticmethod
    def choose_and_swap(string):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        original = string
        string = [i for i in string]

        # get a sorted hash map of characters in string.
        hash_map = sorted(set(string))

        # loop on the characters of the string
        for i in range(len(string)):
            # remove the current character from the set
            hash_map.remove(string[i])

            # if set has become empty, simply return the original string
            if len(hash_map) == 0:
                return original

            # get the least valued character from front of the set.
            character = list(hash_map)[0]

            # if this character is smaller than ith character, change both character and ith character in the string
            # using just one iteration of this nested for loop.
            if ord(character) < ord(string[i]):
                second_character = string[i]
                for j in range(len(string)):
                    if string[j] == character:
                        string[j] = second_character
                    elif string[j] == second_character:
                        string[j] = character
                break

        # return the lexicographically smallest string now.
        return "".join(string)


print(Solution.choose_and_swap("ccad"))
print(Solution.choose_and_swap("abba"))