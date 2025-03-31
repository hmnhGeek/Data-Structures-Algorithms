# Problem link - https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1
# Solution - https://www.youtube.com/watch?v=_gJ3to4RyeQ&t=5632s

from typing import List


class PetrolPump:
    def __init__(self, petrol, next_pump_at):
        self.petrol = petrol
        self.next = next_pump_at


def best_starting_point(petrol_pumps: List[PetrolPump]) -> int:
    # Time complexity is O(N) and space is O(1).

    # initially there is no balance petrol and petrol deficit is also 0.
    net_balance = 0
    petrol_deficit = 0

    # assume the starting pump to be the one at index 0.
    starting_petrol_pump = 0

    # start iterating on all the pumps.
    for i in range(len(petrol_pumps)):
        petrol_pump = petrol_pumps[i]
        net_balance += petrol_pump.petrol - petrol_pump.next
        if net_balance < 0:
            # if the net balance of petrol becomes negative, then it means you cannot
            # start from the current `starting_petrol_pump`. Add the deficit in deficit
            # tracker and start from the `i + 1`th petrol pump with net balance again
            # set to 0.
            petrol_deficit += net_balance
            starting_petrol_pump = i + 1
            net_balance = 0

    # if at the end, after adding net balance to the deficit, we still get some petrol left,
    # then it means that the circular journey is possible, return the starting point.
    if petrol_deficit + net_balance >= 0:
        return starting_petrol_pump

    # else, circular tour is not possible, return -1.
    return -1


def circular_tour(petrol_amount, next_distances):
    # convert petrol pumps to List[PetrolPump] in O(N) time.
    petrol_pumps = []
    for i in range(len(petrol_amount)):
        petrol_pumps.append(PetrolPump(petrol_amount[i], next_distances[i]))
    return best_starting_point(petrol_pumps)


print(circular_tour([4, 6, 7, 4], [6, 5, 3, 5]))
print(circular_tour([6, 3, 7], [4, 6, 3]))