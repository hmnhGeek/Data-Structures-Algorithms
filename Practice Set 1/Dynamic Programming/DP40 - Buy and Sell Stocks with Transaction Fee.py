# Problem link - https://www.naukri.com/code360/problems/rahul-and-his-chocolates_3118974?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=k4eK-vEmnKg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=41


def best_time(prices, fee):
    n = len(prices)
    nxt = {True: 0, False: 0}
    for index in range(n - 1, -1, -1):
        curr = {True: 0, False: 0}
        for can_buy in [True, False]:
            if can_buy:
                curr[can_buy] = max(-prices[index] + nxt[False], nxt[True])
            else:
                curr[can_buy] = max(prices[index] - fee + nxt[True], nxt[False])
        nxt = curr
    return nxt[True]


print(best_time([1, 2, 3], 1))
print(best_time([1, 3, 5, 6], 2))