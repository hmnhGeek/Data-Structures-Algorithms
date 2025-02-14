class Solution:
    @staticmethod
    def _collect(arr, mid):
        w = 0
        for i in range(len(arr)):
            if arr[i] > mid:
                w += (arr[i] - mid)
        return w

    @staticmethod
    def solve(arr, w):
        """
            Time complexity is O(n * log(max(arr))) and space complexity O(1).
        """

        # saw can be on ground to collect max wood or at max ht tree to collect no wood.
        low = 0
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            # get the wood amount collected at mid-ht saw.
            wood_collected = Solution._collect(arr, mid)

            # if wood collected is the required amount, try increasing the ht of the saw to reduce wood destruction.
            if wood_collected == w:
                low = mid + 1

            # if collected wood < w, we must cut more wood, thus reduce high.
            elif wood_collected < w:
                high = mid - 1

            # if > w wood is collected, increase low to reduce wood wastage.
            else:
                low = mid + 1

        # high would point to the correct answer.
        return high


print(Solution.solve([20, 15, 10, 17], 7))
print(Solution.solve([4, 42, 40, 26, 46], 20))
