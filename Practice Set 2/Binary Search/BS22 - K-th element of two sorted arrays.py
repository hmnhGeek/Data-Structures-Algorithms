class Solution:
    @staticmethod
    def find_kth_element(arr1, arr2, k):
        n1, n2 = len(arr1), len(arr2)
        if n1 > n2:
            return Solution.find_kth_element(arr2, arr1, k)
        low = max(0, k - n2)
        high = min(k, n1)
        left = k
        while low <= high:
            mid1 = int(low + (high - low)/2)
            mid2 = left - mid1
            l1 = arr1[mid1 - 1] if 0 <= mid1 - 1 < n1 else -1e6
            l2 = arr2[mid2 - 1] if 0 <= mid2 - 1 < n2 else -1e6
            r1 = arr1[mid1] if 0 <= mid1 < n1 else 1e6
            r2 = arr2[mid2] if 0 <= mid2 < n2 else 1e6
            if l1 > r2:
                high = mid1 - 1
            elif l2 > r1:
                low = mid1 + 1
            elif l1 <= r2 and l2 <= r1:
                return max(l1, l2)
        return -1


print(Solution.find_kth_element([2, 3, 6, 7, 9], [1, 4, 8, 10], 4))
print(Solution.find_kth_element([2, 3, 45], [4, 6, 7, 8], 4))
print(Solution.find_kth_element([1, 2, 3, 5, 6], [4, 7, 8, 9, 100], 6))
print(Solution.find_kth_element([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7))
