class Solution:
    @staticmethod
    def fruits_in_basket(arr):
        n = len(arr)
        baskets = {}
        left, right = 0, 0
        fruits = 0
        start_index = 0
        while right < n:
            if arr[right] not in baskets:
                baskets[arr[right]] = 1
            else:
                baskets[arr[right]] += 1
            if len(baskets) >= 3:
                baskets[arr[left]] -= 1
                if baskets[arr[left]] == 0:
                    del baskets[arr[left]]
                left += 1
            else:
                fruits = max(fruits, right - left + 1)
                start_index = left
            right += 1
        return fruits, arr[start_index:start_index + fruits]


print(Solution.fruits_in_basket([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.fruits_in_basket([1, 2, 1]))
print(Solution.fruits_in_basket([0, 1, 2, 2]))
print(Solution.fruits_in_basket([1, 2, 3, 2, 2]))
print(Solution.fruits_in_basket([3, 1, 2, 2, 2, 2]))
