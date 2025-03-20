class Solution:
    @staticmethod
    def chocola(m, arr):
        # get the cuts costs on horizontal axis
        x = arr[:m - 1]

        # get the cuts costs on vertical axis
        y = arr[m - 1:]

        # sort the costs in descending order in O(n * log(n)) time.
        x.sort(reverse = True)
        y.sort(reverse = True)

        # initially, horizontal and vertical pieces counts are 1.
        horizontal_pieces, vertical_pieces = 1, 1

        # take i, j pointers for traversing the costs array.
        i, j = 0, 0

        # initialize a 0 cost variable.
        cost = 0

        # traverse the arrays now.
        while i < len(x) and j < len(y):
            # use the larger cost first
            if x[i] > y[j]:
                # since we are cutting vertically, multiply the cost with vertical pieces count
                cost += x[i] * vertical_pieces
                # and the horizontal pieces will increase due to this.
                horizontal_pieces += 1
                i += 1
            else:
                # opposite for horizontal cut.
                cost += y[j] * horizontal_pieces
                vertical_pieces += 1
                j += 1

        # do the same for the remaining cuts costs.
        while i < len(x):
            cost += x[i] * vertical_pieces
            horizontal_pieces += 1
            i += 1
        while j < len(y):
            cost += y[j] * horizontal_pieces
            vertical_pieces += 1
            j += 1

        # return the minimum cost.
        return cost


print(Solution.chocola(6, [2, 1, 3, 1, 4, 4, 1, 2]))
