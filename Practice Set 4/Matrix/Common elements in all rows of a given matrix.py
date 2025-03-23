# Problem link - https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/


class Solution:
    @staticmethod
    def get_commons(mtx):
        """
            Time complexity is O(m * n) and space complexity is O(m).
        """

        n, m = len(mtx), len(mtx[0])
        if n == 1:
            return mtx[0]
        set1 = set(mtx[0])
        set2 = set(mtx[1])
        prev = set1.intersection(set2)
        if n == 2:
            return list(prev)
        i = 2
        while i < n:
            prev = prev.intersection(set(mtx[i]))
            i += 1
        return list(prev)


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