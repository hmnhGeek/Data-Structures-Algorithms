# Problem link - https://www.naukri.com/code360/problems/minimum-rate-to-eat-bananas_7449064
# Solution - https://www.youtube.com/watch?v=qyfekrNni90&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=13


from math import ceil


class Solution:
    @staticmethod
    def _is_possible(piles, time_limit, mid):
        time_taken = 0
        for i in range(len(piles)):
            time_taken += ceil(piles[i] / mid)
        return time_taken <= time_limit

    @staticmethod
    def find_rate(piles, time_limit):
        """
            Time complexity is O(n*log(max(arr))) and space complexity is O(1).
        """

        # minimum rate should be 1 banana/hr and max rate should be max(piles) bananas/hr.
        low, high = 1, max(piles)
        while low <= high:
            mid = int(low + (high - low) / 2)
            # check if all the bananas can be eaten within the time limit in O(n) time.
            all_can_be_eaten = Solution._is_possible(piles, time_limit, mid)

            # if they can be, we can reduce the rate as we need to find min rate.
            if all_can_be_eaten:
                high = mid - 1
            else:
                # else we can increase the rate.
                low = mid + 1
        # finally, `low` would point to the correct rate.
        return low


print(Solution.find_rate([3, 6, 7, 11], 8))
print(Solution.find_rate([3, 6, 2, 8], 7))
print(Solution.find_rate([7, 15, 6, 3], 8))
print(Solution.find_rate([25, 12, 8, 14, 19], 5))
print(Solution.find_rate([30, 11, 23, 4, 20], 5))
print(Solution.find_rate([30, 11, 23, 4, 20], 6))
