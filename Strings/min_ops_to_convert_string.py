# Problem link - https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/


class StringConverter:
    @staticmethod
    def _put_front(string, index):
        string = string[index] + string[:index] + string[index + 1:]
        return string

    @staticmethod
    def convert(string1, string2):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        n1 = len(string1)
        n2 = len(string2)

        # if the strings are not of the same length, return
        if n1 != n2:
            return

        # initialize a variable to traverse both the strings.
        i = n1 - 1

        # store the number of operations to 0.
        num_operations = 0

        # while the string traversal is possible...
        while i > 0:
            # if the characters of both the strings at index i do not match.
            if string1[i] != string2[i]:
                # put the ith character of string1 to front.
                string1 = StringConverter._put_front(string1, i)
                # increase the number of operations.
                num_operations += 1
            else:
                # decrement the index i, if the characters do not match.
                i -= 1

        # return the total number of operations.
        return num_operations


print(StringConverter.convert("ABD", "BAD"))
print(StringConverter.convert("EACBD", "EABCD"))
print(StringConverter.convert("GeeksForGeeks", "ForGeeksGeeks"))
print(StringConverter.convert("AbcD", "bcAD"))
print(StringConverter.convert("IFDfxPCdNvCNXPe", "NFfPICxeCNDdXPv"))
