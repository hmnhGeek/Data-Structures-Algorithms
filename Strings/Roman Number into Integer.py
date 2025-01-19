# Problem link - https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1
# Solution - https://www.youtube.com/watch?v=XEDmWJ3PMTY


class Solution:
    mp = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    @staticmethod
    def get_val_of_roman(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(string)
        output = 0
        for i in range(n - 1):
            if Solution.mp[string[i]] < Solution.mp[string[i + 1]]:
                output += (Solution.mp[string[i + 1]] - Solution.mp[string[i]])
                i += 1
            else:
                output += Solution.mp[string[i]]
        if i + 1 < n:
            output += Solution.mp[string[i + 1]]
        return output


print(Solution.get_val_of_roman("IV"))
print(Solution.get_val_of_roman("VII"))
print(Solution.get_val_of_roman("DC"))
print(Solution.get_val_of_roman("XII"))
print(Solution.get_val_of_roman("XIV"))
