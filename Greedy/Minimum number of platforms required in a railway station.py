# Problem link - https://www.geeksforgeeks.org/maximum-trains-stoppage-can-provided/
# Solution - https://www.youtube.com/watch?v=AsGzwR_FWok


class Solution:
    @staticmethod
    def min_platforms(arrivals, departures):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        # sort arrivals and departures so that we can find the overlaps.
        arrivals.sort()
        departures.sort()

        # define tracking variables
        i, j = 0, 0

        # define result variables
        count_min_platforms = 0
        platforms = 0

        # traverse on both the arrays.
        while i < len(arrivals) and j < len(departures):
            # if arrival time is <= departure time during tracking, we need a platform to accommodate
            if arrivals[i] <= departures[j]:
                platforms += 1
                i += 1
            else:
                # if a train has departed, reduce the count of used platforms.
                platforms -= 1
                j += 1

            # update the min platforms required
            count_min_platforms = max(count_min_platforms, platforms)
        return count_min_platforms


print(
    Solution.min_platforms(
        [900, 945, 955, 1100, 1500, 1800],
        [920, 1200, 1130, 1150, 1900, 2000]
    )
)

print(
    Solution.min_platforms(
        [950, 1000, 1015, 1200, 1215],
        [1005, 1030, 1030, 1205, 1230]
    )
)