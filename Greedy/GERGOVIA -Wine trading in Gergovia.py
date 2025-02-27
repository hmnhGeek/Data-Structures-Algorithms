# Problem link - https://www.spoj.com/problems/GERGOVIA/
# Solution - https://www.youtube.com/watch?v=PJdOUDWYstY


class Solution:
    @staticmethod
    def gergovia(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # separate out buy and sell stores with their indices in O(n) time and O(n) space.
        buy, sell = [], []
        for i in range(len(arr)):
            if arr[i] >= 0:
                buy.append([arr[i], i])
            else:
                sell.append([arr[i], i])

        # start iterating on the buy and sell stores in O(n) time.
        i, j, ans = 0, 0, 0
        while i < len(buy) and j < len(sell):
            # get the number of bottles that will be used in the transaction, i.e., min of buyer and seller's bottles.
            bottles = min(buy[i][0], -sell[j][0])

            # give the bottles to buyer.
            buy[i][0] -= bottles
            # and remove the bottles from seller.
            sell[j][0] += bottles

            # compute the cost in transaction using indices and add it to the answer.
            cost = bottles * abs(buy[i][1] - sell[j][1])
            ans += cost

            # if at any point buyer or seller have 0 bottles, then increment their indices respectively.
            if buy[i][0] == 0:
                i += 1
            if sell[j][0] == 0:
                j += 1

        # return the final cost.
        return ans


print(Solution.gergovia([5, -4, 1, -3, 1]))
print(Solution.gergovia([-1000, -1000, -1000, 1000, 1000, 1000]))
