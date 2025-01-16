from math import ceil


class Solution:
    @staticmethod
    def check(n, s, m):
        """
            n – Maximum unit of food you can buy each day.
            s – Number of days you are required to survive.
            m – Unit of food required each day to survive.

            Time complexity is O(1) and space complexity is O(1).
        """

        if n < m:
            return -1
        num_sundays = s//7
        available_days_to_buy = s - num_sundays
        total_food_needed = s * m
        days_food_bought = ceil(total_food_needed/n)
        if days_food_bought <= available_days_to_buy:
            return days_food_bought
        return -1


print(Solution.check(16, 10, 2))
print(Solution.check(20, 10, 30))
