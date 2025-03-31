# Problem link - https://www.geeksforgeeks.org/find-count-number-given-string-present-2d-character-array/
# Solution - https://www.youtube.com/watch?v=ZYeVllg0D7E&t=437s


class Solution:
    @staticmethod
    def _solve(mtx, i, j, word, index, w, n, m):
        # starting (i, j) cell, get the count.
        count = 0

        # if (i, j) matches with word[index]
        if 0 <= i < n and 0 <= j < m and word[index] == mtx[i][j]:
            # then store this character in temp and set (i, j) to 0 to avoid duplicate traversal.
            temp = mtx[i][j]
            mtx[i][j] = 0

            # move to next index
            index += 1

            # if index reached last character, we have found one occurrence and hence count = 1.
            if index == w:
                count = 1
            else:
                # else recursively find the remaining part
                count += Solution._solve(mtx, i, j + 1, word, index, w, n, m)
                count += Solution._solve(mtx, i + 1, j, word, index, w, n, m)
                count += Solution._solve(mtx, i, j - 1, word, index, w, n, m)
                count += Solution._solve(mtx, i - 1, j, word, index, w, n, m)

            # backtrack to (i, j) from 0 to temp
            mtx[i][j] = temp

        # return the count.
        return count

    @staticmethod
    def count(mtx, word):
        """
            Time complexity is O(nm) and space complexity is O(w).
        """

        n, m = len(mtx), len(mtx[0])
        count = 0

        # loop in the matrix and try to find the count of word starting from each cell.
        for i in range(n):
            for j in range(m):
                count += Solution._solve(mtx, i, j, word, 0, len(word), n, m)

        # return the count
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
