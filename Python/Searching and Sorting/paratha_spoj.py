# Problem link - https://www.spoj.com/problems/PRATA/
# Solution - https://www.youtube.com/watch?v=0O91QPfA2xk


from typing import List


def can_be_cooked(num_parathas_required, time_allowed, cook_ranks):
    # This function will run in linear time, i.e., O(L) time.

    # this is the total number of parathas that can be cooked under the allowed time.
    parathas_cooked_till_now = 0

    # we will be starting with the first cook.
    cook_index = 0

    # while we have some cooks to utilize and the number of parathas cooked till now are still lower than required
    while cook_index < len(cook_ranks) and parathas_cooked_till_now < num_parathas_required:
        # get the rank of this cook
        cook_rank = cook_ranks[cook_index]

        # store the time he will take to cook first paratha
        time_taken = cook_rank*1

        # store the parathas cooked by him
        parathas_cooked = 0

        # if he is still within threshold time, let him cook one paratha and then update its time taken for next paratha
        while time_taken <= time_allowed:
            parathas_cooked += 1
            time_taken += cook_rank*(parathas_cooked + 1)

        # if the time taken exceeds the allowed time, then move on to the next cook, but before that, add the parathas
        # cooked by this cook to the overall parathas cooked till now.
        cook_index += 1
        parathas_cooked_till_now += parathas_cooked

    # at the end, just check if we were able to cook the required number of parathas or not.
    return parathas_cooked_till_now >= num_parathas_required


def get_min_time_to_cook(num_parathas_required: int, cook_ranks: List[int]) -> int:
    # Overall time complexity O(L * {log(L * Lmax * p)}) and space taken is O(1).

    # first ensure that you sort the ranks of the cooks because we want to pick those cooks first which are faster in
    # cooking. This will take O(L * log(L)) time where L is the number of cooks or the length of cook_ranks.
    cook_ranks.sort()

    # low and high denote the time units. num_parathas_required can be cooked in min 0 mins (imaginary scenario :))
    # and at max can take max(cook_ranks)*(p *(p + 1)/2) time = cook_ranks[-1]*(p *(p + 1)/2)
    low = 0
    high = cook_ranks[-1]*(num_parathas_required*(num_parathas_required + 1)//2)

    # typical binary search, we have to find that minimum time in which all the required number of parathas can be
    # cooked. Hence, it contributes O(L * log{max(cook_ranks)*(p *(p + 1)/2)}) = O(L * log(Lmax * p)) time.
    while low <= high:
        # get the mid-time value
        mid = int(low + (high - low)/2)

        # check if all or more than required number of parathas can be made in mid-unit time or not in O(L) time.
        all_parathas_can_be_cooked = can_be_cooked(num_parathas_required, mid, cook_ranks)

        if all_parathas_can_be_cooked:
            # if they can be made, then it means we can check for lower values of time.
            high = mid - 1
        else:
            # else we must give more time to the cooks to cook the required number of parathas.
            low = mid + 1

    # as usual, final answer lies in `low` value.
    return low


print(get_min_time_to_cook(3, [1, 3, 1]))
print(get_min_time_to_cook(10, [1, 2, 3, 4]))
print(get_min_time_to_cook(8, [1]*8))
print(get_min_time_to_cook(8, [1]))