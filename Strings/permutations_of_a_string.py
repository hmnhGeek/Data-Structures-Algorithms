from typing import List


class Solution:
    @staticmethod
    def _find_permutations(index, arr, ans, n):
        if index == n:
            result = "".join(arr)
            ans.add(result)
            return

        for i in range(index, n):
            arr[index], arr[i] = arr[i], arr[index]
            Solution._find_permutations(index + 1, arr, ans, n)
            arr[index], arr[i] = arr[i], arr[index]

    @staticmethod
    def get_permutations(string: str):
        arr = [i for i in string]
        ans = set()
        Solution._find_permutations(0, arr, ans, len(arr))
        return ans


print(Solution.get_permutations("ABC"))
print(Solution.get_permutations("AAA"))
print(Solution.get_permutations("ABSG"))