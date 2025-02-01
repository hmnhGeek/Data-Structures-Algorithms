class Solution:
    @staticmethod
    def get_max_points(cards, k):
        """
            Time complexity is O(k) and space complexity is O(1).
        """

        # if the k value is out of scope, return -1
        if k <= 0 or k > len(cards):
            return -1

        # if all the cards are required, return the sum simply.
        if k == len(cards):
            return sum(cards)

        # else initialize i and j
        i = k - 1
        j = len(cards)

        # initialize sums
        _sum = pts = sum(cards[:k])

        # while cards from front can be picked.
        while i >= 0:
            # remove the ith card
            _sum = _sum - cards[i]
            i -= 1
            j -= 1
            # add the jth card
            _sum += cards[j]
            # update the max points obtained.
            pts = max(pts, _sum)

        # return the max points obtained.
        return pts


print(Solution.get_max_points([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(Solution.get_max_points([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution.get_max_points([2, 2, 2], 2))
print(Solution.get_max_points([8, 6, 2, 4, 5], 5))
