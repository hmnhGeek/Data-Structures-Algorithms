class Solution:
    @staticmethod
    def get_longest_consecutive_length(arr):
        mp = set()
        longest_length = 0
        for i in arr:
            mp.add(i)
        for i in arr:
            if i - 1 in mp:
                continue
            j = i
            count = 0
            while j in mp:
                count += 1
                j += 1
            longest_length = max(longest_length, count)
        return longest_length

    @staticmethod
    def get_lcs(arr):
        arr.sort()
        longest_length = 0
        count = 1
        i = 0
        n = len(arr)
        while i < n - 1:
            while i < n - 1 and arr[i + 1] == arr[i] + 1:
                count += 1
                i += 1
            longest_length = max(longest_length, count)
            count = 1
            i += 1
        return longest_length


print(Solution.get_longest_consecutive_length([2, 6, 1, 9, 4, 5, 3]))
print(Solution.get_longest_consecutive_length([1, 9, 3, 10, 4, 20, 2]))
print(Solution.get_longest_consecutive_length([15, 13, 12, 14, 11, 10, 9]))
print(Solution.get_longest_consecutive_length([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]))
print(Solution.get_longest_consecutive_length([100, 4, 200, 1, 3, 2]))
print(Solution.get_longest_consecutive_length([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print()
print(Solution.get_lcs([2, 6, 1, 9, 4, 5, 3]))
print(Solution.get_lcs([1, 9, 3, 10, 4, 20, 2]))
print(Solution.get_lcs([15, 13, 12, 14, 11, 10, 9]))
print(Solution.get_lcs([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]))
print(Solution.get_lcs([100, 4, 200, 1, 3, 2]))
print(Solution.get_lcs([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
