class Solution:
    @staticmethod
    def defense(n, m, mtx):
        xs, ys = [0,], [0, ]
        for i in range(len(mtx)):
            xs.append(mtx[i][0])
            ys.append(mtx[i][1])
        xs.append(n + 1)
        ys.append(m + 1)
        xs.sort()
        ys.sort()
        max_x, max_y = 0, 0
        for i in range(1, len(xs)):
            max_x = max(max_x, xs[i] - xs[i - 1] - 1)
            max_y = max(max_y, ys[i] - ys[i - 1] - 1)
        return max_x * max_y


print(Solution.defense(15, 8, [[3, 8], [11, 2], [8, 6]]))