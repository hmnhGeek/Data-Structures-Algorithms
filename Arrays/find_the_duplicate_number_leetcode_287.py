class DuplicateFinder:
    @staticmethod
    def using_extra_space(arr):
        """
            Overall time complexity is O(n) and overall space complexity is O(n).
        """

        frequencies = dict()
        # This frequencies dictionary will be filled up in O(n) time and will take O(n)
        # space in worst case.
        for i in arr:
            if i not in frequencies:
                frequencies[i] = 1
            else:
                frequencies[i] += 1

        # Additional loop in O(n) time to find the duplicate number.
        for i in frequencies:
            if frequencies[i] > 1:
                return i
        return -1


print(DuplicateFinder.using_extra_space([1, 3, 4, 2, 2]))
print(DuplicateFinder.using_extra_space([3, 1, 3, 4, 2]))
print(DuplicateFinder.using_extra_space([3, 3, 3, 3, 3]))