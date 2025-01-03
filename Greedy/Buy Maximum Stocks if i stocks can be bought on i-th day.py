class Solution:
    @staticmethod
    def buy_stocks(arr, k):
        n = len(arr)
        temp = [(arr[i], i + 1) for i in range(n)]
        temp.sort(key=lambda x: x[0])
        stocks_purchased = 0
        for i in range(n):
            value, limit = temp[i]
            if value * limit <= k:
                stocks_purchased += limit
                k -= (value * limit)
            else:
                rate = k // value
                stocks_purchased += rate
                k -= (rate * value)
        return stocks_purchased


print(Solution.buy_stocks([10, 7, 19], 45))
print(Solution.buy_stocks([7, 10, 4], 100))