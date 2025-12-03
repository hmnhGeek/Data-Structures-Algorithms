# Problem link - https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1


class Solution:
    @staticmethod
    def get_permutations(string):
        """
            Time complexity is O(n! * n) and space complexity is O(n).
        """
        result = set()
        tracker = []
        n = len(string)
        for i in range(len(string)):
            tracker.append(i)
            Solution.solve(tracker, result, n)
            tracker.remove(i)

        final_result = []
        for i in result:
            permutation = ""
            for j in i:
                permutation += string[j]
            final_result.append(permutation)
        return set(final_result)

    @staticmethod
    def solve(tracker, result, n):
        if len(tracker) == n:
            result.add(tuple(tracker))
            return

        for i in range(n):
            if i not in tracker:
                tracker.append(i)
                Solution.solve(tracker, result, n)
                tracker.remove(i)


print(Solution.get_permutations("AAA"))
print(Solution.get_permutations("ABC"))
print(Solution.get_permutations("ABSG"))
