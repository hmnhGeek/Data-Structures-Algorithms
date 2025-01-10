# Problem link - https://www.geeksforgeeks.org/problems/minimum-cost-to-cut-a-board-into-squares/1
# Solution - https://www.youtube.com/watch?v=9DckVBRzuQU


class Solution:
    @staticmethod
    def get_min_cost(costX, costY, n, m):
        """
            Time complexity is O(n * log(n) + m *log(m)) and space complexity is O(1).

            The idea is to make the most expensive cuts first because at the beginning there will be less number of
            pieces to multiply with the cost.
        """

        # set the count of horizontal and vertical cuts to 1 and 1.
        hz_pcs, vr_pcs = 1, 1

        # sort the cost to cut in descending order
        costX.sort(reverse=True)
        costY.sort(reverse=True)

        # reduce n and m to match the available cuts.
        n -= 1
        m -= 1

        # keep pointers at 0th index and min cost variable.
        i, j = 0, 0
        min_cost = 0

        while i < n and j < m:
            # if horizontal cut costs more, let's cut it first
            if costX[i] >= costY[j]:
                min_cost += (costX[i] * vr_pcs)
                # this will increase the count of pieces horizontally.
                hz_pcs += 1
                i += 1
            else:
                # reverse for vertical cuts.
                min_cost += (costY[j] * hz_pcs)
                vr_pcs += 1
                j += 1

        # do the same as merge sort for the remaining items.
        while i < n:
            min_cost += (costX[i] * vr_pcs)
            hz_pcs += 1
            i += 1
        while j < m:
            min_cost += (costY[j] * hz_pcs)
            vr_pcs += 1
            j += 1

        # return the min cost.
        return min_cost


print(Solution.get_min_cost([4, 1, 2], [2, 1, 3, 1, 4], 4, 6))
print(Solution.get_min_cost([1, 1, 1], [1, 1, 1], 4, 4))
