# Problem link - https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1
# Solution - https://www.youtube.com/watch?v=f2ic2Rsc9pU


from typing import List


class Solution:
    @staticmethod
    def _find_permutations(index, arr, ans, n):
        # BASE CASE: if you reach out of bounds, join whatever array has been formed till now and add it to the `ans`.
        if index == n:
            result = "".join(arr)
            ans.add(result)
            return

        # otherwise, loop from index -> n - 1
        for i in range(index, n):
            # swap element at `index` and at `i`
            arr[index], arr[i] = arr[i], arr[index]
            # call the recursion again with index + 1 now as you've moved to the next element.
            Solution._find_permutations(index + 1, arr, ans, n)
            # swap elements back at `index` and at `i` to back track.
            arr[index], arr[i] = arr[i], arr[index]

    @staticmethod
    def get_permutations(string: str):
        """
            Overall time complexity is O(n! * n) and space complexity is O(n! + n).
        """

        # in Python, strings are immutable, therefore, create a copy of string into a list.
        arr = [i for i in string]

        # store a set variable which will store unique permutations.
        ans = set()

        # find the permutations by starting from 0th index.
        Solution._find_permutations(0, arr, ans, len(arr))

        # return the answer.
        return ans


print(Solution.get_permutations("ABC"))
print(Solution.get_permutations("AAA"))
print(Solution.get_permutations("ABSG"))