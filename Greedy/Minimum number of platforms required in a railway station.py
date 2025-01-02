class Solution:
    @staticmethod
    def min_platforms(arrivals, departures):
        arrivals.sort()
        departures.sort()
        i, j = 0, 0
        count_min_platforms = 0
        platforms = 0
        while i < len(arrivals) and j < len(departures):
            if arrivals[i] <= departures[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1
            count_min_platforms = max(count_min_platforms, platforms)
        return count_min_platforms


print(
    Solution.min_platforms(
        [900, 945, 955, 1100, 1500, 1800],
        [920, 1200, 1130, 1150, 1900, 2000]
    )
)