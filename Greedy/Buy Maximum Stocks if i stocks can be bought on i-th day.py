class Solution:
    @staticmethod
    def buy_stocks(arr, k):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        n = len(arr)

        # create a temp array which stores the price of the stock and the max stocks that a person can buy on ith day.
        temp = [(arr[i], i + 1) for i in range(n)]
        # sort this array in O(n * log(n)) time as we want to buy minimum price stocks first
        temp.sort(key=lambda x: x[0])
        # store the number of purchased stocks.
        stocks_purchased = 0

        # loop on the array.
        for i in range(n):
            # extract the stock information
            value, limit = temp[i]

            # if you buy the entire limit of stocks and you've money for that, go ahead.
            if value * limit <= k:
                stocks_purchased += limit
                k -= (value * limit)
            else:
                # else buy only the per unit allowed
                rate = k // value
                stocks_purchased += rate
                k -= (rate * value)

        # return the number of stocks purchased.
        return stocks_purchased


print(Solution.buy_stocks([10, 7, 19], 45))
print(Solution.buy_stocks([7, 10, 4], 100))
print(Solution.buy_stocks([3, 4, 2], 10))
print(Solution.buy_stocks([2, 1], 5))
print(Solution.buy_stocks([10, 12, 11], 30))
print(Solution.buy_stocks([3, 5, 3, 2, 9], 30))
