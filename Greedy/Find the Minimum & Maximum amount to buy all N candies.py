class Solution:
    @staticmethod
    def find_min_max_costs(arr, k):
        arr.sort()
        n = len(arr)
        i, j = 0, n - 1
        min_cost, max_cost = 0, 0
        while i <= j:
            min_cost += arr[i]
            i += 1
            j = j - k
        arr = [arr[i] for i in range(n - 1, -1, -1)]
        i, j = 0, n - 1
        while i <= j:
            max_cost += arr[i]
            i += 1
            j = j - k
        return min_cost, max_cost


print(Solution.find_min_max_costs([3, 2, 1, 4], 2))
print(Solution.find_min_max_costs([3, 2, 1, 4, 5], 4))
