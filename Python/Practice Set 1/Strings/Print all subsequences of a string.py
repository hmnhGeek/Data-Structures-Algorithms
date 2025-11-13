# Problem link - https://www.geeksforgeeks.org/print-subsequences-string/


from typing import List


class Solution:
    @staticmethod
    def get_all_subsequences(string: str) -> List[str]:
        n = len(string)
        result = []
        Solution._solve(string, 0, [], result, n)
        result.sort(key=lambda x: len(x))
        return result

    @staticmethod
    def _solve(string, i, curr, result, n):
        if i == n:
            result.append("".join(curr))
            if len(curr) > 0:
                curr.pop(len(curr) - 1)
            return
        Solution._solve(string, i + 1, curr + [string[i]], result, n)
        Solution._solve(string, i + 1, curr, result, n)


print(Solution.get_all_subsequences("ab"))
print(Solution.get_all_subsequences("abc"))
print(Solution.get_all_subsequences("abcd"))
