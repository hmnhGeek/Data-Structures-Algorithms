class Solution:
    @staticmethod
    def count_of(mtx, word):
        n, m = len(mtx), len(mtx[0])
        count = [0]
        for i in range(n):
            for j in range(m):
                Solution._solve(mtx, word, count, 0, i, j, n, m)
        return count[0]

    @staticmethod
    def _solve(mtx, word, count, idx, i, j, n, m):
        if idx == len(word):
            return 1
        if not (0 <= i < n and 0 <= j < m):
            return 0
        if word[idx] == mtx[i][j]:
            original = mtx[i][j]
            mtx[i][j] = '0'
            up = Solution._solve(mtx, word, count, idx + 1, i - 1, j, n, m)
            right = Solution._solve(mtx, word, count, idx + 1, i, j + 1, n, m)
            down = Solution._solve(mtx, word, count, idx + 1, i + 1, j, n, m)
            left = Solution._solve(mtx, word, count, idx + 1, i, j - 1, n, m)
            if up == 1 or right == 1 or down == 1 or left == 1:
                count[0] += 1
            mtx[i][j] = original


print(
    Solution.count_of(
        [
            ['D', 'D', 'D', 'G', 'D', 'D'],
            ['B', 'B', 'D', 'E', 'B', 'S'],
            ['B', 'S', 'K', 'E', 'B', 'K'],
            ['D', 'D', 'D', 'D', 'D', 'E'],
            ['D', 'D', 'D', 'D', 'D', 'E'],
            ['D', 'D', 'D', 'D', 'D', 'G']
        ],
        "GEEKS"
    )
)

print(
    Solution.count_of(
        [
            ['B', 'B', 'M', 'B', 'B', 'B'],
            ['C', 'B', 'A', 'B', 'B', 'B'],
            ['I', 'B', 'G', 'B', 'B', 'B'],
            ['G', 'B', 'I', 'B', 'B', 'B'],
            ['A', 'B', 'C', 'B', 'B', 'B'],
            ['M', 'C', 'I', 'G', 'A', 'M']
        ],
        "MAGIC"
    )
)

print(
    Solution.count_of(
        [
            ['S', 'N', 'B', 'S', 'N'],
            ['B', 'A', 'K', 'E', 'A'],
            ['B', 'K', 'B', 'B', 'K'],
            ['S', 'E', 'B', 'S', 'E']
        ],
        "SNAKES"
    )
)

print(
    Solution.count_of(
        [
            ['c', 'a', 't'],
            ['a', 't', 'c'],
            ['c', 't', 'a']
        ],
        "cat"
    )
)
