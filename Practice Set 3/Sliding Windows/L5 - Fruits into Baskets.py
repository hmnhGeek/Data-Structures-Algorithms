class Solution:
    @staticmethod
    def solve(arr):
        left = right = 0
        n = len(arr)
        d = {i: 0 for i in arr}
        max_collected = 0
        start_index = -1
        while right < n:
            d[arr[right]] += 1
            if sum(1 for v in d.values() if v != 0) > 2:
                d[arr[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v != 0) <= 2:
                max_collected = max(max_collected, right - left + 1)
                start_index = left
            right += 1
        return arr[start_index:start_index + max_collected] if start_index != -1 else []


print(Solution.solve([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution.solve([1, 2, 1]))
print(Solution.solve([0, 1, 2, 2]))
print(Solution.solve([1, 2, 3, 2, 2]))
print(Solution.solve([3, 1, 2, 2, 2, 2]))
print(Solution.solve([1, 1, 2, 3]))
print(Solution.solve([1, 2, 3, 4]))
