# Problem link - https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1
# Solution - https://www.youtube.com/watch?v=3jdxYj3DD98


class Solution:
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    @staticmethod
    def convert(roman):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        num = 0
        for i in range(len(roman) - 1):
            a, b = roman[i], roman[i + 1]
            if Solution.mapping[a] < Solution.mapping[b]:
                num -= Solution.mapping[a]
            else:
                num += Solution.mapping[a]
        num += Solution.mapping[roman[len(roman) - 1]]
        return num


print(Solution.convert("IX"))
print(Solution.convert("XL"))
print(Solution.convert("MCMIV"))
