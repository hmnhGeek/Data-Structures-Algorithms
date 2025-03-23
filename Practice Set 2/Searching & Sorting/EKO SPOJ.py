class Solution:
    @staticmethod
    def _wood_collected(arr, mid):
        n = len(arr)
        wood = 0
        for i in range(n):
            if arr[i] > mid:
                wood += arr[i] - mid
        return wood

    @staticmethod
    def eko(arr, k):
        if k < 0:
            return -1

        # saw can be on ground to collect max wood or at max ht tree to collect no wood.
        low = 0
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)

            # get the wood amount collected at mid-ht saw.
            wood_collected = Solution._wood_collected(arr, mid)

            # if wood collected is the required amount or greater than it, try increasing the ht of the saw to reduce
            # wood destruction.
            if wood_collected >= k:
                low = mid + 1

            # if collected wood < w, we must cut more wood, thus reduce high.
            else:
                high = mid - 1

        # high would point to the correct answer.
        return high


print(Solution.eko([20, 15, 10, 17], 7))
print(Solution.eko([4, 42, 40, 26, 46], 20))
