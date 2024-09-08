def group_strings(strings):
    groups = dict()
    for string in strings:
        counts = [0] * 26
        for char in string:
            counts[ord(char) - ord("a")] += 1
        counts = tuple(counts)
        if counts in groups:
            groups[counts].append(string)
        else:
            groups[counts] = [string]
    return list(groups.values())


print(group_strings(["act", "god", "cat", "dog", "tac"]))
print(group_strings(["no", "on", "is"]))
