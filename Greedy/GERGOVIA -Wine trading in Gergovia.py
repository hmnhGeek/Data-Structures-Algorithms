# Problem link - https://www.spoj.com/problems/GERGOVIA/
# Solution - https://www.youtube.com/watch?v=PJdOUDWYstY


class Solution:
    @staticmethod
    def gergovia(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        buy, sell = [], []
        for i in range(len(arr)):
            if arr[i] >= 0:
                buy.append([arr[i], i])
            else:
                sell.append([arr[i], i])
        i, j, ans = 0, 0, 0
        while i < len(buy) and j < len(sell):
            bottles = min(buy[i][0], -sell[j][0])
            buy[i][0] -= bottles
            sell[j][0] += bottles
            cost = bottles * abs(buy[i][1] - sell[j][1])
            ans += cost
            if buy[i][0] == 0:
                i += 1
            if sell[j][0] == 0:
                j += 1
        return ans


print(Solution.gergovia([5, -4, 1, -3, 1]))
print(Solution.gergovia([-1000, -1000, -1000, 1000, 1000, 1000]))
