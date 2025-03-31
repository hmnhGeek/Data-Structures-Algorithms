# Problem link - https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/


class Matrix:
    @staticmethod
    def _transpose(mtx, n):
        for i in range(1, n):
            for j in range(i):
                mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]

    @staticmethod
    def rotate(mtx):
        """
            Overall time complexity is O(n^2) and space is O(1).
        """

        n = len(mtx)
        # This will take O(n^2) time
        Matrix._transpose(mtx, n)
        # this will also take O(n^2) time.
        for i in range(n):
            mtx[i] = mtx[i][-1:-n-1:-1]

    @staticmethod
    def show(mtx):
        for i in mtx:
            print(i)


m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Matrix.rotate(m1)
Matrix.show(m1)
print()
m2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
Matrix.rotate(m2)
Matrix.show(m2)