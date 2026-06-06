class Solution:
    @staticmethod
    def _find_first_positive(arr, i, n):
        while i < n and arr[i] < 0:
            i += 1
        if i >= n:
            return None
        return i

    @staticmethod
    def _find_first_negative(arr, i, n):
        while i < n and arr[i] >= 0:
            i += 1
        if i >= n:
            return None
        return i

    @staticmethod
    def rearrange(arr):
        n = len(arr)
        is_positive = True
        for i in range(n):
            ai = arr[i]
            if is_positive and ai < 0:
                idx = Solution._find_first_positive(arr, i + 1, n)
                if idx is not None:
                    arr[i], arr[idx] = arr[idx], arr[i]
            elif not is_positive and ai < 0:
                pass
            elif is_positive and ai >= 0:
                pass
            else:
                idx = Solution._find_first_negative(arr, i + 1, n)
                if idx is not None:
                    arr[i], arr[idx] = arr[idx], arr[i]
            is_positive = not is_positive
        print(arr)


Solution.rearrange([1, 2, 3, -4, -1, 4])
Solution.rearrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])
