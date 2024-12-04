class Solution:
    @staticmethod
    def fruits_into_baskets(arr):
        n = len(arr)
        left = right = 0
        max_fruits = 0
        start_index = -1
        d = {i: 0 for i in arr}
        while right < n:
            d[arr[right]] += 1
            if sum(1 for v in d.values() if v != 0) > 2:
                d[arr[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v != 0) <= 2:
                max_fruits = max(max_fruits, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index + max_fruits]


print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
