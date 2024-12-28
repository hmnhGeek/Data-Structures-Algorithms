class Solution:
    @staticmethod
    def get_fractional_knapsack(values, weights, capacity):
        n = len(values)

        # collect the information in a separate array holding both (values, capacity) of each item. This will take O(n)
        # extra space.
        arr = [(values[i], weights[i]) for i in range(n)]

        # now sort this array in descending order of their value/unit weight. This will take O(n * log(n)) time.
        arr.sort(key=lambda x: x[0]/x[1], reverse=True)

        # create a variable to store the collected value.
        collected_value = 0

        # now loop on each item in O(n) time.
        for item in arr:
            value, weight = item

            # multiply the per-unit weight value with whatever is minimum, i.e., if the bag capacity left if less than
            # the item weight, take only whatever the bag allows, else take the entire weight value of the item.
            collected_value += (value/weight) * min(capacity, weight)

            # now reduce the capacity of the bag by the amount of weight taken.
            capacity -= min(capacity, weight)

            # if the bag is full, no need for the rest of the for loop. Simply break out.
            if capacity == 0:
                break

        # return the collected value.
        return collected_value


print(Solution.get_fractional_knapsack([100, 60, 100, 200], [20, 10, 50, 50], 90))