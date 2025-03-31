# Problem link - https://www.geeksforgeeks.org/print-subsequences-string/


class Solution:
    @staticmethod
    def _solve(string, index, subseq, subsequences):
        # if the string gets exhausted
        if index < 0:
            # append the generated subsequence into subsequences.
            subsequence = [i for i in subseq]
            subsequences.append("".join(subsequence))
            return
        # solve recursively by including character at index.
        Solution._solve(string, index - 1, [string[index],] + subseq, subsequences)
        # solve recursively by not including character at index.
        Solution._solve(string, index - 1, subseq, subsequences)

    @staticmethod
    def get_all_subsequences(string):
        """
            Time complexity would be O(2^n) and space complexity would be O(n).
        """
        n = len(string)
        subsequences = []
        # update subsequences array.
        Solution._solve(string, n - 1, [], subsequences)
        # return subsequences.
        return subsequences


print(Solution.get_all_subsequences("ab"))
print(Solution.get_all_subsequences("abc"))
print(Solution.get_all_subsequences("abcd"))