from typing import List


def can_be_cooked(num_parathas_required, time_allowed, cook_ranks):
    parathas_cooked_till_now = 0
    cook_index = 0

    while cook_index < len(cook_ranks) and parathas_cooked_till_now < num_parathas_required:
        cook_rank = cook_ranks[cook_index]
        time_taken = cook_rank
        parathas_cooked = 0

        while time_taken <= time_allowed:
            parathas_cooked += 1
            time_taken += cook_rank*(parathas_cooked + 1)

        cook_index += 1
        parathas_cooked_till_now += parathas_cooked

    return parathas_cooked_till_now >= num_parathas_required


def get_min_time_to_cook(num_parathas_required: int, cook_ranks: List[int]) -> int:
    cook_ranks.sort()
    low = 0
    high = cook_ranks[-1]*(num_parathas_required*(num_parathas_required + 1)//2)

    while low <= high:
        mid = int(low + (high - low)/2)
        all_parathas_can_be_cooked = can_be_cooked(num_parathas_required, mid, cook_ranks)

        if all_parathas_can_be_cooked:
            high = mid - 1
        else:
            low = mid + 1

    return low


# print(can_be_cooked(3, 3, [1, 1, 3]))
print(get_min_time_to_cook(3, [1, 3, 1]))
print(get_min_time_to_cook(10, [1, 2, 3, 4]))
print(get_min_time_to_cook(8, [1]*8))
print(get_min_time_to_cook(8, [1]))