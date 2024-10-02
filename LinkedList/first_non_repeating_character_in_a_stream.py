class UsingDictionary:
    @classmethod
    def get_non_repeating(cls, d):
        # This will take O(26) time and O(26) space, practically O(1) time and O(1) space.
        # get the first character with count = 1
        for i in d:
            if d[i] == 1:
                return i

        # if all of them have a count != 1, return '#'.
        return '#'

    @staticmethod
    def first_non_repeating(string):
        """
            Overall time complexity is O(n) and space complexity is O(26) = O(1).
        """

        # create a blank counter for each character in order. A python dictionary maintains order which is
        # necessary here.
        d = {}
        for i in string:
            d[i] = 0

        result = ""
        # loop in the string and increment the counter of each character; this takes O(n) time.
        for i in string:
            d[i] += 1
            # at the same time, find the first character in the dictionary which has a count of 1, that's
            # why the order matters here.
            result += UsingDictionary.get_non_repeating(d)
        # return the result.
        return result


print("Using python dictionary...")
print(UsingDictionary.first_non_repeating("abcbbac"))
print(UsingDictionary.first_non_repeating("zz"))
print(UsingDictionary.first_non_repeating("aabc"))
print(UsingDictionary.first_non_repeating("geeksforgeeksandgeeksquizfor"))
print(UsingDictionary.first_non_repeating("aabcbc"))
print(UsingDictionary.first_non_repeating("abadbc"))
print(UsingDictionary.first_non_repeating("abcabc"))
