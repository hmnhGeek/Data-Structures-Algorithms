class Solution:
    @staticmethod
    def get_kth(arr1, arr2, k):
        n1, n2 = len(arr1), len(arr2)
        if k not in range(n1 + n2):
            return
        if n1 > n2:
            return Solution.get_kth(arr2, arr1, k)
        low = max(k - n2, 0)
        high = min(k, n1)
        left = k
        n = n1 + n2
        while low <= high:
            mid1 = int(low + (high - low) / 2)
            mid2 = left - mid1
            l1 = arr1[mid1 - 1] if mid1 - 1 >= 0 else -1e6
            l2 = arr2[mid2 - 1] if mid2 - 1 >= 0 else -1e6
            r1 = arr1[mid1] if mid1 < n1 else 1e6
            r2 = arr2[mid2] if mid2 < n2 else 1e6
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return -1


print(Solution.get_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 4))
print(Solution.get_kth([2, 3, 45], [4, 6, 7, 8], 4))
print(Solution.get_kth([1, 2, 3, 5, 6], [4, 7, 8, 9, 100], 6))
