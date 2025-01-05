class Solution:
    @staticmethod
    def _solve(mtx, i, j, word, index, w, n, m):
        count = 0
        if 0 <= i < n and 0 <= j < m and word[index] == mtx[i][j]:
            temp = mtx[i][j]
            mtx[i][j] = 0
            index += 1
            if index == w:
                count = 1
            else:
                count += Solution._solve(mtx, i, j + 1, word, index, w, n, m)
                count += Solution._solve(mtx, i + 1, j, word, index, w, n, m)
                count += Solution._solve(mtx, i, j - 1, word, index, w, n, m)
                count += Solution._solve(mtx, i - 1, j, word, index, w, n, m)
            mtx[i][j] = temp
        return count

    @staticmethod
    def count(mtx, word):
        n, m = len(mtx), len(mtx[0])
        count = 0
        for i in range(n):
            for j in range(m):
                count += Solution._solve(mtx, i, j, word, 0, len(word), n, m)
        return count


print(
    Solution.count(
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
    Solution.count(
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
    Solution.count(
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
    Solution.count(
        [
            ['c', 'a', 't'],
            ['a', 't', 'c'],
            ['c', 't', 'a']
        ],
        "cat"
    )
)
