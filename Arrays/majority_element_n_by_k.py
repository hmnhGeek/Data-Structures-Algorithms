from collections import Counter


class Solution:
    @staticmethod
    def get_majority_elements(arr, k):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # if k is 0 or negative, return -1.
        if k <= 0:
            return -1

        # get the length of the array.
        n = len(arr)

        # find n/k value
        nbyk = n // k

        # get the frequencies of the array elements in O(n) time and O(n) space.
        frequencies = Counter(arr)

        # loop on all the elements in the frequencies dictionary
        for element in frequencies:
            # and if the frequency of any element > n/k, print it.
            if frequencies[element] > nbyk:
                print(element, end=" ")
        print()


Solution.get_majority_elements([3, 1, 2, 2, 1, 2, 3, 3], 4)
Solution.get_majority_elements([9, 8, 7, 9, 2, 9, 7], 3)