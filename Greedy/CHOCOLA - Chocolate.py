class Solution:
    @staticmethod
    def chocola(m, arr):
        x = arr[:m - 1]
        y = arr[m - 1:]
        x.sort(reverse = True)
        y.sort(reverse = True)
        horizontal_pieces, vertical_pieces = 1, 1
        i, j = 0, 0
        cost = 0
        while i < len(x) and j < len(y):
            if x[i] > y[j]:
                cost += x[i] * vertical_pieces
                horizontal_pieces += 1
                i += 1
            else:
                cost += y[j] * horizontal_pieces
                vertical_pieces += 1
                j += 1
        while i < len(x):
            cost += x[i] * vertical_pieces
            horizontal_pieces += 1
            i += 1
        while j < len(y):
            cost += y[j] * horizontal_pieces
            vertical_pieces += 1
            j += 1
        return cost


print(Solution.chocola(6, [2, 1, 3, 1, 4, 4, 1, 2]))
