class Solution:
    @staticmethod
    def are_isomorphic(s1, s2):
        if len(s1) != len(s2):
            return False
        mp = {}
        for i in range(len(s1)):
            ss = s1[i]
            tt = s2[i]
            if (ss in mp and mp[ss] != tt) or (ss not in mp and tt in mp.values()):
                return False
            mp[ss] = tt
        return True


print(Solution.are_isomorphic("add", "egg"))
print(Solution.are_isomorphic("purple", "title"))
print(Solution.are_isomorphic("aab", "xyz"))
print(Solution.are_isomorphic("aab", "xxy"))
print(Solution.are_isomorphic("bbbaaaba", "aaabbbba"))