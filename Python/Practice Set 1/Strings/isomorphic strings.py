class Solution:
    @staticmethod
    def are_isomorphic(s1, s2):
        # if the length of the strings are not same, return false.
        if len(s1) != len(s2):
            return False

        # initialize a map to store characters.
        mp = {}
        for i in range(len(s1)):
            ss = s1[i]
            tt = s2[i]

            # if the mp[ss] != tt or tt is present already as a value but not for this ss key, then return false.
            if (ss in mp and mp[ss] != tt) or (ss not in mp and tt in mp.values()):
                return False

            # ss --> tt
            mp[ss] = tt

        # return True finally.
        return True


print(Solution.are_isomorphic("add", "egg"))
print(Solution.are_isomorphic("purple", "title"))
print(Solution.are_isomorphic("aab", "xyz"))
print(Solution.are_isomorphic("aab", "xxy"))
print(Solution.are_isomorphic("bbbaaaba", "aaabbbba"))
