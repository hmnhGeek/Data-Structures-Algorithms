from math import ceil


class Solution:
    @staticmethod
    def _is_possible(piles, time_limit, mid):
        time_taken = 0
        for i in range(len(piles)):
            time_taken += ceil(piles[i]/mid)
        return time_taken <= time_limit

    @staticmethod
    def find_rate(piles, time_limit):
        low, high = 1, max(piles)
        while low <= high:
            mid = int(low + (high - low)/2)
            all_can_be_eaten = Solution._is_possible(piles, time_limit, mid)
            if all_can_be_eaten:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.find_rate([3, 6, 7, 11], 8))
print(Solution.find_rate([3, 6, 2, 8], 7))
print(Solution.find_rate([7, 15, 6, 3], 8))
print(Solution.find_rate([25, 12, 8, 14, 19], 5))