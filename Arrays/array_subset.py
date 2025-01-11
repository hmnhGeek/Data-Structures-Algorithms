# Problem link - https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1


class Solution:
    @staticmethod
    def is_subset(a, b):
        """
            We are checking for b in `a`.

            Time complexity is O(m + n) and space complexity is O(n).
        """

        # if b is of size greater than that of a, then b cannot be a subset of a.
        if len(b) > len(a):
            return False
        m, n = len(a), len(b)

        # initialize a dictionary of size `n` which will store the status of b's elements found in a.
        found_status = {i: False for i in b}

        # now loop in `a`.
        for i in range(m):
            # if a[i] is present in dictionary, mark it as found.
            if a[i] in found_status:
                found_status[a[i]] = True

        # b will be a subset of a only if all found_status values are True.
        return all(v for v in found_status.values())


print(Solution.is_subset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))
print(Solution.is_subset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))
print(Solution.is_subset([10, 5, 2, 23, 19], [19, 5, 3]))
print(Solution.is_subset([2, 1, 8, 6, 4, 9, 3], [3, 4, 7]))
