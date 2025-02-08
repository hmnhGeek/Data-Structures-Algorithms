class Solution:
    @staticmethod
    def fruits_into_baskets(arr):
        left = right = 0
        n = len(arr)
        d = {i: 0 for i in arr}
        count = 0
        start_index = -1
        while right < n:
            d[arr[right]] += 1
            if sum(1 for v in d.values() if v > 0) > 2:
                d[arr[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v > 0) <= 2:
                count = max(count, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index+count] if start_index != -1 else []


print(Solution.fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_into_baskets([1, 2, 1]))
print(Solution.fruits_into_baskets([0, 1, 2, 2]))
print(Solution.fruits_into_baskets([1, 2, 3, 2, 2]))
print(Solution.fruits_into_baskets([3, 1, 2, 2, 2, 2]))
print(Solution.fruits_into_baskets([1, 1, 2, 3]))
print(Solution.fruits_into_baskets([1, 2, 3, 4]))
