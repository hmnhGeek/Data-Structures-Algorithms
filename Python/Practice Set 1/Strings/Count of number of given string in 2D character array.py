# Problem link - https://www.geeksforgeeks.org/find-count-number-given-string-present-2d-character-array/
# Solution - https://www.youtube.com/watch?v=ZYeVllg0D7E&t=437s


class Solution:
    @staticmethod
    def count_of(mtx, word):
        n, m = len(mtx), len(mtx[0])
        count = [0]

        # initiate searches from each cell.
        for i in range(n):
            for j in range(m):
                Solution._solve(mtx, word, count, 0, i, j, n, m)
        return count[0]

    @staticmethod
    def _solve(mtx, word, count, idx, i, j, n, m):
        # if we have exhausted all the characters of the word, we found it, return 1.
        if idx == len(word):
            return 1

        # if (i, j) does not exist, return 0
        if not (0 <= i < n and 0 <= j < m):
            return 0

        # if w_idx = mtx(i, j), lets perform recursive calls
        if word[idx] == mtx[i][j]:
            # mark the current cell as '0' to avoid infinite loops
            original = mtx[i][j]
            mtx[i][j] = '0'

            # recursively check for neighbouring cells.
            up = Solution._solve(mtx, word, count, idx + 1, i - 1, j, n, m)
            right = Solution._solve(mtx, word, count, idx + 1, i, j + 1, n, m)
            down = Solution._solve(mtx, word, count, idx + 1, i + 1, j, n, m)
            left = Solution._solve(mtx, word, count, idx + 1, i, j - 1, n, m)

            # if word is found in any of the paths, increment the count
            if up == 1 or right == 1 or down == 1 or left == 1:
                count[0] += 1

            # backtrack
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
