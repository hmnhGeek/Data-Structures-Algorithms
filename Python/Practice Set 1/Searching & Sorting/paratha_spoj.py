# Problem link - https://www.spoj.com/problems/PRATA/
# Solution - https://www.youtube.com/watch?v=0O91QPfA2xk


class Solution:
    @staticmethod
    def _if_possible(ranks, mid, num_required):
        cooked_parathas = 0
        cook = 0
        while cook < len(ranks) and cooked_parathas < num_required:
            rank = ranks[cook]
            time_taken = rank * 1
            parathas_by_this_cook = 0
            while time_taken <= mid:
                parathas_by_this_cook += 1
                time_taken += rank * (parathas_by_this_cook + 1)
            cooked_parathas += parathas_by_this_cook
            cook += 1
        return cooked_parathas >= num_required

    @staticmethod
    def get_min_time_to_cook(num_required, ranks):
        ranks.sort()
        low, high = 0, ranks[-1] * (num_required * (num_required + 1)//2)
        while low <= high:
            mid = int(low + (high - low)/2)
            all_parathas_can_be_cooked = Solution._if_possible(ranks, mid, num_required)
            if all_parathas_can_be_cooked:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.get_min_time_to_cook(3, [1, 3, 1]))
print(Solution.get_min_time_to_cook(10, [1, 2, 3, 4]))
print(Solution.get_min_time_to_cook(8, [1]*8))
print(Solution.get_min_time_to_cook(8, [1]))
