class LinearSolution:
    @staticmethod
    def minimize_the_max_distance(arr, k):
        """
            Time complexity is O(nk) and space complexity is O(n).
        """

        # edge case
        if k <= 0:
            return -1

        # store the length of the array in `n` for easier access.
        n = len(arr)

        # create a (n - 1) length list of 0s storing the count of gas stations placed inside the ith slot. This should
        # take O(n) space.
        how_many = [0] * (n - 1)

        # now start placing the k gas stations in O(n * k) time.
        for gas_station in range(k):
            # for each iteration, let us try to find the slot with maximum difference as that is the one which we want
            # to minimize.
            max_slot = -1e6
            max_slot_index = -1

            # now loop on the slots in O(n) time.
            for i in range(n - 1):
                # get the slot difference
                slot_difference = arr[i + 1] - arr[i]
                # check what would be the new slot difference if we place a gas station inside this slot.
                new_slot_difference = slot_difference/(how_many[i] + 1)
                # new_slot_difference is directly proportional to slot_difference and so we can use it to updat the max
                # slot.
                if max_slot < new_slot_difference:
                    max_slot = new_slot_difference
                    max_slot_index = i

            # once the max_slot_index is found, add a gas station in that slot.
            how_many[max_slot_index] += 1

        ############ FINDING THE MAXIMUM DISTANCE IN THE UPDATED ARRAY AFTER GAS STATIONS PLACEMENTS ################

        # let's assume that the max distance between any two gas stations is -inf.
        minimum_max_distance = -1e6

        # loop on the slots in O(n) time.
        for i in range(n - 1):
            # get the evenly distributed gas stations distance at this slot.
            slot_difference = (arr[i + 1] - arr[i])/(how_many[i] + 1)
            # and take the maximum distance.
            minimum_max_distance = max(minimum_max_distance, slot_difference)

        # finally return the max distance.
        return minimum_max_distance


print(LinearSolution.minimize_the_max_distance([1,2,3,4,5,6,7], 6))
print(LinearSolution.minimize_the_max_distance([1, 2, 3, 4, 5], 4))
print(LinearSolution.minimize_the_max_distance(list(range(1, 11)), 1))