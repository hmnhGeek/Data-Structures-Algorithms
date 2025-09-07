# Problem link - https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/


from collections import Counter


class Solution:
    @staticmethod
    def find_commons(mtx):
        """
            Time complexity is O(nm) and space complexity is O(m)
        """
        n, m = len(mtx), len(mtx[0])
        temp = dict(Counter(mtx[0]))
        for i in range(1, n):
            row = dict(Counter(mtx[i]))
            for j in temp:
                if j in row:
                    temp[j] = min(temp[j], row[j])
                else:
                    temp[j] = 0
        result = []
        for i in temp:
            if temp[i] > 0:
                result.append(i)

        return result


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
