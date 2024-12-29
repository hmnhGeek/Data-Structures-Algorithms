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
        # create a resultant string which will store the numerical form of the string.
        result = ""

        # create a blank dictionary for the repeated characters, so that we don't have to loop again.
        cache = {}

        # loop in the string now.
        for character in string:
            # if the character was already checked in previously, directly add it to result from the cache.
            if character in cache:
                result += cache[character]
                continue

            # else loop in the keypad
            for key in Solution._keypad:
                # if the character's key is found.
                if character in Solution._keypad[key]:
                    # start a pointer from 0.
                    j = 0
                    # extract the sequence stored in this key.
                    sequence = Solution._keypad[key]

                    # for this character, let's get the numerical sequence in this variable.
                    key_seq = ""
                    while j < len(sequence) and sequence[j] != character:
                        # add the key to key_seq until the character is found.
                        key_seq += str(key)
                        # also, update the cache for sequence[j] while figuring out for this character.
                        cache[sequence[j]] = key_seq
                        j += 1

                    # when the character is matched, add key one last time.
                    key_seq += str(key)

                    # update the result
                    result += key_seq

                    # update the cache for this character
                    cache[character] = key_seq

                    # break, as we have found the character and no further iterations are needed.
                    break

        # return the result finally.
        return result


print(Solution.get_numeric_representation("GEEKSFORGEEKS"))
print(Solution.get_numeric_representation("HELLO WORLD"))
print(Solution.get_numeric_representation("GFG"))
print(Solution.get_numeric_representation("HEY U"))
print(Solution.get_numeric_representation("CODINGNINJAS"))
print(Solution.get_numeric_representation("PREPINSTA"))
