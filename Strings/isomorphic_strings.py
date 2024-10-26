def is_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    s2t = dict()
    t2s = dict()
    for i in range(len(s1)):
        if s1[i] not in s2t:
            s2t[s1[i]] = s2[i]
        else:
            if s2t[s1[i]] != s2[i]:
                return False

        if s2[i] not in t2s:
            t2s[s2[i]] = s1[i]
        else:
            if t2s[s2[i]] != s1[i]:
                return False
    return True


print(is_isomorphic("add", "egg"))
print(is_isomorphic("purple", "title"))
print(is_isomorphic("aab", "xyz"))
print(is_isomorphic("aab", "xxy"))
print(is_isomorphic("bbbaaaba", "aaabbbba"))