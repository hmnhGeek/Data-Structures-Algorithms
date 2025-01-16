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

        # find the actual number of days you can buy the food (excluding sundays)
        num_sundays = s//7
        available_days_to_buy = s - num_sundays

        # find the amount of food needed to survive in total
        total_food_needed = s * m

        # find the number of days you're required to buy to store the complete ration.
        days_food_bought = ceil(total_food_needed/n)

        # if the days required to buy < available days to buy, return answer.
        if days_food_bought <= available_days_to_buy:
            return days_food_bought

        # else return -1.
        return -1


print(Solution.check(16, 10, 2))
print(Solution.check(20, 10, 30))
