# Problem link - https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/


class Solution:
    @staticmethod
    def get_commons(mtx):
        """
            Time complexity is O(nm) and space complexity is O(m).
        """

        n, m = len(mtx), len(mtx[0])
        if n == 1:
            return mtx[0]

        # get the common elements into a hashmap of size O(m) in worst case by taking into account common elements from
        # the first two rows.
        hash_map = set(mtx[0]).intersection(set(mtx[1]))

        # now loop on the rest of the rows...
        for i in range(2, n):
            # form a temp set in O(m) time for this ith row
            temp_set = set(mtx[i])
            # take intersection with hashmap in another O(m) time to filter out only the common elements into hashmap.
            hash_map = hash_map.intersection(temp_set)

        # finally, return the hashmap storing all the common elements in the matrix.
        return hash_map


print(
    Solution.get_commons(
        [
            [1, 2, 1, 4, 8],
            [3, 7, 8, 5, 1],
            [8, 7, 7, 3, 1],
            [8, 1, 2, 7, 9]
        ]
    )
)