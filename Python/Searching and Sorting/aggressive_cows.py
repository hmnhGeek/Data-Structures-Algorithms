# Problem link - https://www.naukri.com/code360/problems/aggressive-cows_1082559
# Solution - https://www.youtube.com/watch?v=R_Mfw4ew-Vo&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=18

def cows_can_be_placed(stalls, minimum_distance_between_stalls, num_cows):
    # This will take O(n) time and O(1) space.

    # let's place the first cow at index 0 always greedily.
    cows_placed = 1
    last_cow_placed_at_index = 0

    for i in range(1, len(stalls)):
        # if the distance between the current stall and the last stall where a cow was placed,
        # is more than the minimum distance required, let's place another cow at this index,
        # and update the last cow placed at index value.
        if stalls[i] - stalls[last_cow_placed_at_index] >= minimum_distance_between_stalls:
            cows_placed += 1
            last_cow_placed_at_index = i

    # if we were able to place at least num_cows with a minimum distance, return True, else False.
    return cows_placed >= num_cows


def aggressive_cows(stalls, num_cows):
    # Overall time complexity is O(n*log(n)) and O(1) space complexity.

    # takes O(n*log(n)) time. We can sort because it won't affect the final result, as the `stalls` array
    # actually tells the position of the stalls and not the relative distance. To compute the relative
    # distance we can sort the stalls and then take differences between the positions.
    stalls.sort()

    # minimum distance between any two stalls will always be 1.
    low = 1
    # maximum distance between any two stalls will be (max - min) when only two cows can be placed, isn't it?
    high = max(stalls) - min(stalls)

    # this will take a time complexity of O(n*log(max - min)) and O(1) space.
    while low <= high:
        mid = int(low + (high - low)/2)

        # check that can we place all the `num_cows` number of cows in the stalls with at least a distance
        # of mid-units?
        if cows_can_be_placed(stalls, mid, num_cows):
            # let's try to increase the minimum distance more and check if some higher distance can also
            # be used to place all the cows?
            low = mid + 1
        else:
            # if all the cows cannot be placed with a minimum distance of `mid` between the stalls, let
            # us reduce the distance between the stalls.
            high = mid - 1

    return high


def prettify(stalls, num_cows):
    print(f"A maximum of {aggressive_cows(stalls, num_cows)} units distance is required to place all {num_cows} cows in stalls at positions {stalls}.")


prettify([0, 3, 4, 7, 10, 9], 4)
prettify([4, 2, 1, 3, 6], 2)