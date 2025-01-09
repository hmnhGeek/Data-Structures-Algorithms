# Problem link - https://www.geeksforgeeks.org/problems/shop-in-candy-store1145/1
# Solution - https://www.youtube.com/watch?v=2Sj6-5JFaAo


class Solution:
    @staticmethod
    def find_min_max_costs(arr, k):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """

        # sort the costs in increasing order in O(n * log(n)) time.
        arr.sort()
        n = len(arr)

        # point i and j at 0 and n - 1 indices.
        i, j = 0, n - 1

        # set min and max costs
        min_cost, max_cost = 0, 0

        # now loop in the increasing array
        while i <= j:
            # buy the min cost candies
            min_cost += arr[i]
            i += 1
            # and since you can get at most k candies free on each buy, take the most expensive ones for free.
            j = j - k

        # for max cost, now reverse the array
        arr = [arr[i] for i in range(n - 1, -1, -1)]
        i, j = 0, n - 1
        while i <= j:
            # buy the expensive ones
            max_cost += arr[i]
            i += 1
            # get the cheapest ones for free.
            j = j - k

        # return max and min cost to get all the candies.
        return min_cost, max_cost


print(Solution.find_min_max_costs([3, 2, 1, 4], 2))
print(Solution.find_min_max_costs([3, 2, 1, 4, 5], 4))
print(Solution.find_min_max_costs([9, 8, 2, 6, 4], 2))
print(Solution.find_min_max_costs([1, 5, 4], 0))
