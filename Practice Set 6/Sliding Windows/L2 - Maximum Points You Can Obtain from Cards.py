class Solution:
    @staticmethod
    def get_max_points(cards, k):
        if k <= 0 or k > len(cards):
            return -1
        if k == len(cards):
            return sum(cards)
        i = k - 1
        j = len(cards)
        _sum = pts = sum(cards[:k])
        while i >= 0:
            _sum = _sum - cards[i]
            i -= 1
            j -= 1
            _sum += cards[j]
            pts = max(pts, _sum)
        return pts


print(Solution.get_max_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.get_max_points([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.get_max_points([2, 2, 2], 2))
print(Solution.get_max_points([8, 6, 2, 4, 5], 5))
