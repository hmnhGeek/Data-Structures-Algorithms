def bruteforce():
    def counter(string):
        d = {}
        for i in string:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return d

    def num_substrings_with_all_three_chars(string):
        n = len(string)
        result = []
        for i in range(n):
            for j in range(i, n):
                substr = string[i:j]
                counts = counter(substr)
                if len(counts) == 3:
                    result.append(substr)
        return result

    print(num_substrings_with_all_three_chars("bbacba"))


bruteforce()