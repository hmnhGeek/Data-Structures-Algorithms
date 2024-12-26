class Solution:
    @staticmethod
    def _num_gas_stations_placed(arr, mid, n):
        count = 0
        for i in range(n - 1):
            gas_stations = (arr[i + 1] - arr[i]) // mid
            if gas_stations * mid == arr[i + 1] - arr[i]:
                gas_stations -= 1
            count += gas_stations
        return count

    @staticmethod
    def minimize_distance(arr, k):
        if k <= 0:
            return

        # low and high denote the distance where gas stations can be placed.
        # assume you can place all the gas stations at 0 max-distance only.
        low = 0

        # assume high to be 0 for now; we will make it point to current max distance between all the gas stations.
        high = 0
        n = len(arr)

        # for n - 1 slots, update `high` to point to the max distance, because we have to minimize the distance. We
        # cannot place outside the array bounds, as that will only increase the distance.
        for i in range(n - 1):
            high = max(high, arr[i + 1] - arr[i])

        # as per question, we are allowed to have error variance of 10^(-6).
        delta = 1e-6

        # while the variance is more than delta...
        while high - low > delta:
            # compute mid, or the assumed max-distance. We cannot have any two gas stations placed in such a way that
            # the distance between them is more than this mid-distance. Let's see if we can place exactly k-gas stations
            # with this mid-distance or not.
            mid = (low + high) / 2

            # find the number of gas stations place with at max mid-distance.
            num_placed = Solution._num_gas_stations_placed(arr, mid, n)

            # if we require more than `k` gas stations just to maintain mid-distance as max permissible distance between
            # k gas stations, then we must increase this mid-distance so that we require less gas stations to maintain
            # the max distance value.
            if num_placed > k:
                low = mid
            else:
                # else, this would mean that we were able to place <= k gas stations with mid-distance as max
                # permissible distance between any two consecutive gas stations. Since we need to minimize this max
                # distance, let's reduce `high` now.
                high = mid

        # finally, `high` would point to the correct max-distance that has been minimized.
        return high


print(Solution.minimize_distance([1, 2, 3, 4, 5, 6, 7], 6))
print(Solution.minimize_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.minimize_distance([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))
print(Solution.minimize_distance([1, 13, 17, 23], 5))
