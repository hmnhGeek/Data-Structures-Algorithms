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
        """
            Overall time complexity is O(n + {n! * n} + n! + {n! * log(n!)} + n!) and space complexity is O(n + n!).
        """

        n = len(arr)
        # in O(n) time, get the numerical representation. Also takes O(n) space internally.
        number = Solution._get_numerical_representation(arr)

        # get the unique permutations in O(n! * n) time and O(n! + n) space.
        permutations = set()
        Solution._get_next_permutation(arr, 0, n, permutations)

        # convert into list in O(n!) time.
        permutations = list(permutations)
        # sort in O(n! * log(n!))
        permutations.sort()

        # get index of input arr in O(n!) time.
        index_of_arr = permutations.index(tuple(arr))

        # return answer in O(1) time.
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
    def _get_breakpoint_index(arr, n):
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                return i
        return None

    @staticmethod
    def _swap_breakpoint(arr, breakpoint_index, n):
        for i in range(n - 1, breakpoint_index, -1):
            if arr[i] > arr[breakpoint_index]:
                arr[i], arr[breakpoint_index] = arr[breakpoint_index], arr[i]
                break

    @staticmethod
    def get_next_permutation(arr):
        n = len(arr)
        breakpoint_index = OptimalSolution._get_breakpoint_index(arr, n)
        if breakpoint_index is None:
            OptimalSolution._reverse(arr, 0, n - 1)
            return
        OptimalSolution._swap_breakpoint(arr, breakpoint_index, n)
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