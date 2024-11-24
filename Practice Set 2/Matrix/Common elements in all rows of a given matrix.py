from collections import Counter


class Solution:
    @staticmethod
    def find_commons(mtx):
        n, m = len(mtx), len(mtx[0])
        reference_dict = dict(Counter(mtx[0]))
        for i in range(1, n):
            row_dict = {}
            for j in range(m):
                if mtx[i][j] not in row_dict:
                    row_dict[mtx[i][j]] = 1
                else:
                    row_dict[mtx[i][j]] += 1
            for k in reference_dict:
                if k in row_dict:
                    reference_dict[k] = min(reference_dict[k], row_dict[k])
                else:
                    reference_dict[k] = 0
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