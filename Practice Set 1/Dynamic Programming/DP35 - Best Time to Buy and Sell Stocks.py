# Problem link - https://www.naukri.com/code360/problems/stocks-are-profitable_893405?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=excAOvwF_Wk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=36


def best_time(prices):
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    n = len(prices)
    min_price_till_now = 1e6
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, prices[i] - min_price_till_now)
        min_price_till_now = min(min_price_till_now, prices[i])
    return max_profit


print(best_time([7, 1, 5, 3, 6, 4]))
print(best_time([2, 100, 150, 120]))
print(best_time([1, 2, 3, 4]))
print(best_time([2, 2, 2, 2]))
print(best_time([17, 20, 11, 9, 12, 6]))
print(best_time([98, 101, 66, 72]))