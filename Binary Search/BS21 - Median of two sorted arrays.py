class Solution:
    @staticmethod
    def find_median(arr1, arr2):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # define length variables.
        n1 = len(arr1)
        n2 = len(arr2)
        n = n1 + n2

        # define median variables as Nones
        elem1, elem2 = None, None

        # define pointers and a counter variable
        i, j = 0, 0
        counter = 0

        # merging from the two sorted arrays
        while i < len(arr1) and j < len(arr2):
            # increment the counter first
            counter += 1

            # if the counter has reached n/2, its elem1 turn
            if counter == n // 2:
                elem1 = min(arr1[i], arr2[j])
            # if the counter has reached n/2 + 1, its elem2 turn
            if counter == (n // 2) + 1:
                elem2 = min(arr1[i], arr2[j])

            # typical merge() function code
            if arr1[i] <= arr2[j]:
                i += 1
            else:
                j += 1

        while i < len(arr1):
            # same logic as above for counter, but this time just use arr1 instead of taking a min.
            counter += 1
            if counter == n // 2:
                elem1 = arr1[i]
            if counter == (n // 2) + 1:
                elem2 = arr1[i]
            i += 1

        while j < len(arr2):
            # same logic as above for counter, but this time just use arr2 instead of taking a min.
            counter += 1
            if counter == n // 2:
                elem1 = arr2[j]
            if counter == (n // 2) + 1:
                elem2 = arr2[j]
            j += 1

        # return the median
        if n % 2 == 0:
            return (elem1 + elem2) / 2
        return elem2


print(Solution.find_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.find_median([1, 3, 4], [2, 6]))
print(Solution.find_median([1, 3], [2]))
print(Solution.find_median([1, 2], [3, 4]))