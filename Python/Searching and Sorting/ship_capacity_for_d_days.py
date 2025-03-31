# Problem link - https://www.naukri.com/code360/problems/capacity-to-ship-packages-within-d-days_1229379

def shipment_possible_within_req_days(weights, mid, days):
    # This will consume O(n) time and O(1) space.
    consumed_days = 0
    consumed_capacity = 0

    for i in range(len(weights)):
        # add the weights continuously until you do not overload the ship capacity.
        if consumed_capacity + weights[i] <= mid:
            consumed_capacity += weights[i]
        else:
            # the current weight if added, overflows the capacity, then increase
            # the day count (meaning that one day is consumed), and then you can
            # freely assign the current weight to the consumed_capacity, meaning
            # the next day has started.
            if consumed_capacity != 0:
                consumed_days += 1
            consumed_capacity = weights[i]

    # if after consuming all the weights the consumed capacity is still not zero,
    # then push it to next day. Updating consumed_day = 0 is now optional.
    if consumed_capacity != 0:
        consumed_days += 1

    # return True if consumed days is within days threshold, else False.
    return consumed_days <= days


def get_min_ship_capacity(weights, days):
    # Overall time complexity is O(n * log(sum - max)) and overall space complexity is O(1).

    # please give at least one day to ship right?
    if days == 0 or len(weights) == 0:
        return -1

    # at least max(weights) is required to ship all the packages (not concerned with number days consumed).
    # at max sum(weights) is required to ship all the packages in one day.
    low, high = max(weights), sum(weights)

    # This will consume O(n * log(sum - max)) and O(1) space.
    while low <= high:
        mid = int(low + (high - low)/2)

        if shipment_possible_within_req_days(weights, mid, days):
            # if the shipment is possible <= days using mid-capacity,
            # let's see if we can reduce capacity further to maintain
            # the days' threshold.
            high = mid - 1
        else:
            # if it was not possible with mid-capacity within days,
            # let's increase the capacity of the ship to be within
            # days threshold.
            low = mid + 1

    return low


print(get_min_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(get_min_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(get_min_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(get_min_ship_capacity([11], 1))
print(get_min_ship_capacity([], 2))
