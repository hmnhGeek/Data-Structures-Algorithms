class Solution:
    @staticmethod
    def get_commons(mtx):
        n, m = len(mtx), len(mtx[0])
        if n == 1:
            return mtx[0]
        hash_map = set(mtx[0]).intersection(set(mtx[1]))
        for i in range(2, n):
            temp_set = set(mtx[i])
            hash_map = hash_map.intersection(temp_set)
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