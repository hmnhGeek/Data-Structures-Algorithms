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
        # Time complexity is O(N^2) and space complexity is O(1) (the counter dictionary will have at most
        # 3 keys only).

        n = len(string)
        result = 0
        for i in range(n):
            for j in range(i, n):
                substr = string[i:j+1]
                counts = counter(substr)
                if len(counts) == 3:
                    result += 1
        return result

    print(num_substrings_with_all_three_chars("bbacba"))
    print(num_substrings_with_all_three_chars("abcabc"))
    print(num_substrings_with_all_three_chars("aaacb"))
    print(num_substrings_with_all_three_chars("abc"))


def optimal():
    def counter(string):
        d = {}
        for i in string:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return d

    def num_substrings_with_all_three_chars(string):
        # Time complexity is O(N^2) and space complexity is O(1) (the counter dictionary will have at most
        # 3 keys only).

        n = len(string)
        result = 0
        for i in range(n):
            for j in range(i, n):
                substr = string[i:j+1]
                counts = counter(substr)
                if len(counts) == 3:
                    result += 1
        return result

    print(num_substrings_with_all_three_chars("bbacba"))
    print(num_substrings_with_all_three_chars("abcabc"))
    print(num_substrings_with_all_three_chars("aaacb"))
    print(num_substrings_with_all_three_chars("abc"))


def optimal():
    def get_num_substrings(string):
        # Overall time complexity is O(N) and space complexity is O(1).
        i, j = 0, 0
        result = 0
        counter = {"a": 0, "b": 0, "c": 0}

        # This will take O(N) time
        while j < len(string):
            if not all(v != 0 for k, v in counter.items()):
                counter[string[j]] += 1
                j += 1
            else:
                result += (len(string) - (j - 1))
                counter[string[i]] -= 1
                i += 1

        # This will take another O(N) time.
        while all(v != 0 for k, v in counter.items()):
            result += 1
            counter[string[i]] -= 1
            i += 1

        return result

    print(get_num_substrings("bbacba"))
    print(get_num_substrings("abcabc"))
    print(get_num_substrings("aaacb"))
    print(get_num_substrings("abc"))



bruteforce()
print()
optimal()