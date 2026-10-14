# Problem link - https://www.geeksforgeeks.org/problems/find-the-string-in-grid0111/1
# Solution - https://www.youtube.com/watch?v=lM4bTtF6yuk


class Solution:
    @staticmethod
    def get_all_occurrences(mtx, word):
        """
            Time complexity is O(n * m * k) and space complexity is O(k).
        """
        result = []
        n, m = len(mtx), len(mtx[0])
        dir_x = [-1, -1, 0, 1, 1, 1, 0, -1]
        dir_y = [0, 1, 1, 1, 0, -1, -1, -1]
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == word[0]:
                    for di in range(8):
                        x = dir_x[di]
                        y = dir_y[di]
                        word_formed = Solution._check_if_word_formed(i, j, 0, x, y, word, mtx)
                        if word_formed:
                            result.append((i, j))
        return result

    @staticmethod
    def _check_if_word_formed(i, j, k, x, y, word, mtx):
        if k == len(word):
            return True
        if not (0 <= i < len(mtx) and 0 <= j < len(mtx[0])):
            return False
        if mtx[i][j] != word[k]:
            return False
        if Solution._check_if_word_formed(i + x, j + y, k + 1, x, y, word, mtx):
            return True
        return False


print(
    Solution.get_all_occurrences(
        [
            ['a', 'b', 'a', 'b'],
            ['a', 'b', 'e', 'b'],
            ['e', 'b', 'e', 'b']
        ], "abe"
    )
)

print(
    Solution.get_all_occurrences(
        [
            ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S'],
            ['G', 'E', 'E', 'K', 'S', 'Q', 'U', 'I', 'Z', 'G', 'E', 'E', 'K'],
            ['I', 'D', 'E', 'Q', 'A', 'P', 'R', 'A', 'C', 'T', 'I', 'C', 'E']
        ], "GEEKS"
    )
)
