class Solution:
    @staticmethod
    def get_min_cost(costX, costY, n, m):
        hz_pcs, vr_pcs = 1, 1
        costX.sort(reverse=True)
        costY.sort(reverse=True)
        n -= 1
        m -= 1
        i, j = 0, 0
        min_cost = 0
        while i < n and j < m:
            if costX[i] >= costY[j]:
                min_cost += (costX[i] * vr_pcs)
                hz_pcs += 1
                i += 1
            else:
                min_cost += (costY[j] * hz_pcs)
                vr_pcs += 1
                j += 1
        while i < n:
            min_cost += (costX[i] * vr_pcs)
            hz_pcs += 1
            i += 1
        while j < m:
            min_cost += (costY[j] * hz_pcs)
            vr_pcs += 1
            j += 1
        return min_cost


print(Solution.get_min_cost([4, 1, 2], [2, 1, 3, 1, 4], 4, 6))