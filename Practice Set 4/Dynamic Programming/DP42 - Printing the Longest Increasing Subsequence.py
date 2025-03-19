class Solution:
    @staticmethod
    def print_lis(arr):
        n = len(arr)
        dp = {i: 1 for i in range(n)}
        parents = {i: i for i in range(n)}
        for i in range(n):
            for prev in range(i):
                if arr[prev] < arr[i]:
                    if 1 + dp[prev] > dp[i]:
                        dp[i] = 1 + dp[prev]
                        parents[i] = prev
        last_element_index_of_lis = max(dp, key=dp.get)
        j = last_element_index_of_lis
        lis = []
        while parents[j] != j:
            lis.append(arr[j])
            j = parents[j]
        lis.append(arr[j])
        return lis[-1:-len(lis)-1:-1]


print(Solution.print_lis([5, 4, 11, 1, 16, 8]))
print(Solution.print_lis([1, 2, 2]))
print(Solution.print_lis([10, 20, 3, 40]))
print(Solution.print_lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(Solution.print_lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(Solution.print_lis([1]))
print(Solution.print_lis([5, 6, 3, 4, 7, 6]))
print(Solution.print_lis([1, 2, 3, 4, 5]))
