# Problem link - https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
# Solution - https://www.youtube.com/watch?v=1ibsQrnuEEg


class Solution:
    @staticmethod
    def get_fractional_knapsack(values, weights, capacity):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        n = len(values)

        # collect the information in a separate array holding both (values, capacity) of each item. This will take O(n)
        # extra space.
        arr = [(values[i], weights[i]) for i in range(n)]

        # now sort this array in descending order of their value/unit weight. This will take O(n * log(n)) time.
        arr.sort(key=lambda x: x[0] / x[1], reverse=True)

        # create a variable to store the collected value.
        collected_value = 0

        # now loop on each item in O(n) time.
        for item in arr:
            value, weight = item

            # multiply the per-unit weight value with whatever is minimum, i.e., if the bag capacity left if less than
            # the item weight, take only whatever the bag allows, else take the entire weight value of the item.
            collected_value += (value / weight) * min(capacity, weight)

            # now reduce the capacity of the bag by the amount of weight taken.
            capacity -= min(capacity, weight)

            # if the bag is full, no need for the rest of the for loop. Simply break out.
            if capacity == 0:
                break

        # return the collected value.
        return collected_value


print(Solution.get_fractional_knapsack([100, 60, 100, 200], [20, 10, 50, 50], 90))
print(Solution.get_fractional_knapsack([60, 100, 120], [10, 20, 30], 50))
print(Solution.get_fractional_knapsack([60, 100], [10, 20], 50))
print(Solution.get_fractional_knapsack([10, 20, 30], [5, 10, 15], 100))
print(Solution.get_fractional_knapsack([500], [30], 10))
print(Solution.get_fractional_knapsack([3, 6, 1, 4], [6, 1, 5, 3], 10))
print(Solution.get_fractional_knapsack([40, 50, 25, 100, 30, 45], [50, 40, 90, 120, 10, 200], 200))
print(Solution.get_fractional_knapsack([12, 35, 41, 25, 32], [20, 24, 36, 40, 42], 100))

