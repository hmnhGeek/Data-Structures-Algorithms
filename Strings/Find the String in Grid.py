class Solution:
    @staticmethod
    def _exists(grid, string, i, j, n, m, s, dir_x, dir_y):
        found = False
        for direction in range(8):
            i1, j1 = i, j
            x1, y1 = dir_x[direction], dir_y[direction]
            k = 0
            while 0 <= i1 < n and 0 <= j1 < m and k < s:
                if string[k] == grid[i1][j1]:
                    i1 += x1
                    j1 += y1
                    k += 1
                else:
                    break
            found = found or k == s
        return found

    @staticmethod
    def find_string(grid, string):
        result = []
        dir_x = [-1, 0, 1, 1, 1, 0, -1, -1]
        dir_y = [1, 1, 1, 0, -1, -1, -1, 0]
        n, m, s = len(grid), len(grid[0]), len(string)
        for i in range(n):
            for j in range(m):
                if Solution._exists(grid, string, i, j, n, m, s, dir_x, dir_y):
                    result.append((i, j))
        return result


print(Solution.find_string(
    [
        ["a", "b", "c"],
        ["d", "r", "f"],
        ["g", "h", "i"]
    ],
    "abc")
)

print(
    Solution.find_string(
        [['a', 'b', 'a', 'b'],
         ['a', 'b', 'e', 'b'],
         ['e', 'b', 'e', 'b']],
        "abe"
    )
)
