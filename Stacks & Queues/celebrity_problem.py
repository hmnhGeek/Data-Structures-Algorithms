class Solution:
    @staticmethod
    def find_celebrity(mtx):
        n = len(mtx)
        top, down = 0, n - 1

        while top < down:
            if mtx[top][down] == 1:
                top += 1
            elif mtx[down][top] == 1:
                down -= 1
            else:
                top += 1
                down -= 1

        if top == down:
            for i in range(n):
                if top != i and mtx[top][i] == 1:
                    return -1
            for i in range(n):
                if top != i and mtx[i][top] == 0:
                    return -1
            return top
        return -1


print(Solution.find_celebrity([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]))
print(Solution.find_celebrity([[0, 1], [1, 0]]))
print(Solution.find_celebrity([[0]]))
print(Solution.find_celebrity([[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]))
