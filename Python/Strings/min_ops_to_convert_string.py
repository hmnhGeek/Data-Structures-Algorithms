# Problem link - https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/
# Solution - https://www.youtube.com/watch?v=mv5eeYHOYiI

from collections import Counter


class StringConverter:
    @staticmethod
    def convert(string1, string2):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        n1 = len(string1)
        n2 = len(string2)

        # if the strings are not of the same length or if both of them do not have exactly same characters, return
        if n1 != n2 or Counter(string1) != Counter(string2):
            return -1

        # initialize a variable to traverse both the strings.
        i = n1 - 1
        j = n2 - 1

        # store the number of operations to 0.
        num_operations = 0

        # while the string traversal is possible...
        while i >= 0:
            # if the characters of both the strings do not match...
            if string1[i] != string2[j]:
                # increase the number of operations.
                num_operations += 1
            else:
                # decrement the index j, if the characters match.
                j -= 1
            # irrespective, decrement index i.
            i -= 1

        # return the total number of operations.
        return num_operations


print(StringConverter.convert("ABD", "BAD"))
print(StringConverter.convert("EACBD", "EABCD"))
print(StringConverter.convert("GeeksForGeeks", "ForGeeksGeeks"))
print(StringConverter.convert("AbcD", "bcAD"))
print(StringConverter.convert("IFDfxPCdNvCNXPe", "NFfPICxeCNDdXPv"))
