class Solution:
    @staticmethod
    def _get_numerical_representation(arr):
        reversed = arr[-1:-len(arr)-1:-1]
        number = 0
        for i in range(len(arr)):
            number += (reversed[i] * 10 ** i)
        return number

    @staticmethod
    def _get_next_permutation(arr, index, n, permutations):
        if index == n:
            temp = [i for i in arr]
            permutations.append(temp)
            return
        for i in range(index, n):
            arr[index], arr[i] = arr[i], arr[index]
            Solution._get_next_permutation(arr, index + 1, n, permutations)
            arr[index], arr[i] = arr[i], arr[index]

    @staticmethod
    def get_next_permutation(arr):
        n = len(arr)
        number = Solution._get_numerical_representation(arr)
        permutations = []
        Solution._get_next_permutation(arr, 0, n, permutations)
        permutations.sort(key=lambda x: Solution._get_numerical_representation(x))
        index_of_arr = permutations.index(arr)
        if 0 <= index_of_arr + 1 < len(permutations):
            return permutations[index_of_arr + 1]
        return permutations[0]


print(Solution.get_next_permutation([1, 2, 3]))
print(Solution.get_next_permutation([1, 1, 5]))
print(Solution.get_next_permutation([3, 2, 1]))
print(Solution.get_next_permutation([2, 4, 1, 7, 5, 0]))
print(Solution.get_next_permutation([3, 4, 2, 5, 1]))
print(Solution.get_next_permutation([2, 3, 1, 5, 4]))