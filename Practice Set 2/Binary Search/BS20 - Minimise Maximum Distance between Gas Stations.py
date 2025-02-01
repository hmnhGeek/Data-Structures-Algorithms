class LinearSolution:
    @staticmethod
    def minimize_the_max_distance(arr, k):
        if k <= 0:
            return -1
        n = len(arr)
        how_many = [0] * (n - 1)
        for gas_station in range(k):
            max_slot = -1e6
            max_slot_index = -1
            for i in range(n - 1):
                slot_difference = arr[i + 1] - arr[i]
                new_slot_difference = slot_difference/(how_many[i] + 1)
                if max_slot < new_slot_difference:
                    max_slot = new_slot_difference
                    max_slot_index = i
            how_many[max_slot_index] += 1
        minimum_max_distance = -1e6
        for i in range(n - 1):
            slot_difference = (arr[i + 1] - arr[i])/(how_many[i] + 1)
            minimum_max_distance = max(minimum_max_distance, slot_difference)
        return minimum_max_distance


print(LinearSolution.minimize_the_max_distance([1,2,3,4,5,6,7], 6))
print(LinearSolution.minimize_the_max_distance([1, 2, 3, 4, 5], 4))
print(LinearSolution.minimize_the_max_distance(list(range(1, 11)), 1))