# Problem link - https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1


def is_isomorphic(s1, s2):
    """
        Time complexity is O(n) and space complexity is O(n) when all n characters are unique.
    """

    # if the length of the strings do not match, they are not isomorphic.
    if len(s1) != len(s2):
        return False

    # initialize two hash maps storing directions of the character mapping.
    s2t = dict()
    t2s = dict()

    # start the loop on indices.
    for i in range(len(s1)):
        # if character from s1 is not in s2t, add a direction from s1[i] --> s2[i]
        if s1[i] not in s2t:
            s2t[s1[i]] = s2[i]
        else:
            # if the mapping already exists, and you're encountering it for the next time,
            # check if the s2[i] is same from s2t mapping. If not, strings are not isomorphic.
            if s2t[s1[i]] != s2[i]:
                return False

        # if character from s2 is not in t2s, add a direction from s2[i] --> s1[i]
        if s2[i] not in t2s:
            t2s[s2[i]] = s1[i]
        else:
            # if the mapping already exists, and you're encountering it for the next time,
            # check if the s1[i] is same from t2s mapping. If not, strings are not isomorphic.
            if t2s[s2[i]] != s1[i]:
                return False

    # return True as strings are isomorphic.
    return True


print(is_isomorphic("add", "egg"))
print(is_isomorphic("purple", "title"))
print(is_isomorphic("aab", "xyz"))
print(is_isomorphic("aab", "xxy"))
print(is_isomorphic("bbbaaaba", "aaabbbba"))