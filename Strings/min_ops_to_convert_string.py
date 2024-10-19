class StringConverter:
    @staticmethod
    def _put_front(string, index):
        string = string[index] + string[:index] + string[index + 1:]
        return string

    @staticmethod
    def convert(string1, string2):
        n1 = len(string1)
        n2 = len(string2)
        if n1 != n2:
            return
        i, j = n1 - 1, n2 - 1
        num_operations = 0
        while i > 0 and j > 0:
            if string1[i] != string2[j]:
                string1 = StringConverter._put_front(string1, i)
                num_operations += 1
            else:
                i -= 1
                j -= 1
        return num_operations


print(StringConverter.convert("ABD", "BAD"))
print(StringConverter.convert("EACBD", "EABCD"))
print(StringConverter.convert("GeeksForGeeks", "ForGeeksGeeks"))
