class Solution:
    @staticmethod
    def get_min_jumps(arr):
        n = len(arr)
        if n == 0:
            return -1
        if n == 1:
            return 0

        max_reach = 0
        last_index = 0
        jumps = 0
        for i in range(n):
            max_reach = max(max_reach, i + arr[i])
            if i == last_index:
                if max_reach == i:
                    return -1
                last_index = max_reach
                jumps += 1
                if max_reach >= n - 1:
                    return jumps
        return jumps
    

print(Solution.get_min_jumps([1, 2, 3, 1, 1, 0, 2, 5]))
print(Solution.get_min_jumps([1, 2, 4, 1, 1, 0, 2, 5]))
print(Solution.get_min_jumps([1, 4, 3, 2, 6, 7]))
print(Solution.get_min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(Solution.get_min_jumps([0, 10, 20]))
print(Solution.get_min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution.get_min_jumps([2, 3, 1, 1, 4]))
print(Solution.get_min_jumps([2, 3, 0, 1, 4]))
