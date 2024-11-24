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
            permutations.add(tuple(temp))
            return
        for i in range(index, n):
            arr[index], arr[i] = arr[i], arr[index]
            Solution._get_next_permutation(arr, index + 1, n, permutations)
            arr[index], arr[i] = arr[i], arr[index]

    @staticmethod
    def get_next_permutation(arr):
        n = len(arr)
        number = Solution._get_numerical_representation(arr)
        permutations = set()
        Solution._get_next_permutation(arr, 0, n, permutations)
        permutations = list(permutations)
        permutations.sort()
        index_of_arr = permutations.index(tuple(arr))
        if 0 <= index_of_arr + 1 < len(permutations):
            return list(permutations[index_of_arr + 1])
        return list(permutations[0])


class OptimalSolution:
    @staticmethod
    def _reverse(arr, low, high):
        while low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    @staticmethod
    def get_next_permutation(arr):
        n = len(arr)
        breakpoint_index = None
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                breakpoint_index = i
                break
        if breakpoint_index is None:
            OptimalSolution._reverse(arr, 0, n - 1)
            return
        for i in range(n - 1, breakpoint_index, -1):
            if arr[i] > arr[breakpoint_index]:
                arr[i], arr[breakpoint_index] = arr[breakpoint_index], arr[i]
                break
        OptimalSolution._reverse(arr, breakpoint_index + 1, n - 1)


print(Solution.get_next_permutation([1, 2, 3]))
print(Solution.get_next_permutation([1, 1, 5]))
print(Solution.get_next_permutation([3, 2, 1]))
print(Solution.get_next_permutation([2, 4, 1, 7, 5, 0]))
print(Solution.get_next_permutation([3, 4, 2, 5, 1]))
print(Solution.get_next_permutation([2, 3, 1, 5, 4]))
print()


def test(*args):
    l = [i for i in args]
    OptimalSolution.get_next_permutation(l)
    print(l)


test(1, 2, 3)
test(1, 1, 5)
test(3, 2, 1)
test(2, 4, 1, 7, 5, 0)
test(3, 4, 2, 5, 1)
test(2, 3, 1, 5, 4)