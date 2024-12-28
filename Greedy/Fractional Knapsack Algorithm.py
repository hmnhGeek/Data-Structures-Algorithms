class Solution:
    @staticmethod
    def get_fractional_knapsack(values, weights, capacity):
        n = len(values)
        arr = [(values[i], weights[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0]/x[1], reverse=True)
        collected_value = 0
        for item in arr:
            value, weight = item
            collected_value += (value/weight)*min(capacity, weight)
            capacity -= min(capacity, weight)
        return collected_value


print(Solution.get_fractional_knapsack([100, 60, 100, 200], [20, 10, 50, 50], 90))