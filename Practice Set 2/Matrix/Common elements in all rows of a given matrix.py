# Problem link - https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/


from collections import Counter


class Solution:
    @staticmethod
    def find_commons(mtx):
        """
            Time complexity is O(n * 3m) and space complexity is O(m) for the dictionaries.
        """

        # get the dimensions of the matrix.
        n, m = len(mtx), len(mtx[0])

        # initialize a reference dictionary by using the first row of the matrix. This will take O(m) time and O(m)
        # space when all elements are unique in the worst case.
        reference_dict = dict(Counter(mtx[0]))

        # loop in the matrix from 1st row (0th used above).
        for i in range(1, n):
            # create a counter dictionary for ith row.
            row_dict = {}

            # loop in the columns of this row in O(m) time.
            for j in range(m):
                # increment the count of (i, j) cell in row_dict.
                if mtx[i][j] not in row_dict:
                    row_dict[mtx[i][j]] = 1
                else:
                    row_dict[mtx[i][j]] += 1

            # now loop in the reference dictionary in O(m) time and take the minimum count for each key which is found
            # both reference dictionary and row dictionary. Why min? To ensure that at the end we get the correct
            # common count.
            for k in reference_dict:
                if k in row_dict:
                    reference_dict[k] = min(reference_dict[k], row_dict[k])
                else:
                    # if there is no key `k` found in row dictionary, then set its value to 0 in reference dict because
                    # we cannot delete directly from a dictionary while inside a loop.
                    reference_dict[k] = 0
            # update reference dictionary with non-zero valued keys in O(m) time.
            reference_dict = {k: v for k, v in reference_dict.items() if v != 0}
        return list(reference_dict.keys())


print(
    Solution.find_commons(
        [
            [1, 2, 1, 4, 8],
            [3, 7, 8, 5, 1],
            [8, 7, 7, 3, 1],
            [8, 1, 2, 7, 9]
        ]
    )
)

print(
    Solution.find_commons(
        [
            [1, 4, 5, 6],
            [3, 4, 5, 6],
            [5, 6, 7, 2]
        ]
    )
)

print(
    Solution.find_commons(
        [
            [4, 6],
            [6, 4],
            [2, 6]
        ]
    )
)

print(
    Solution.find_commons(
        [
            [1, 2, 3],
            [2, 2, 3],
            [2, 3, 1],
            [2, 3, 4]
        ]
    )
)

print(
    Solution.find_commons(
        [
            [1, 2, 3],
            [0, 6, 0],
            [4, 6, 1]
        ]
    )
)