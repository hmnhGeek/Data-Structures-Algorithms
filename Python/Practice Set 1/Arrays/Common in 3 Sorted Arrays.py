# Problem link - https://www.geeksforgeeks.org/problems/common-elements1132/1


class Solution:
    @staticmethod
    def find_common(a, b, c):
        """
            Time complexity is O({n, m, p}) and space complexity is O(1).
        """
        i, j, k = 0, 0, 0
        result = []
        n, m, p = len(a), len(b), len(c)
        while i < n and j < m and k < p:
            if a[i] == b[j] == c[k]:
                if len(result) == 0:
                    result.append(a[i])
                elif result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
                k += 1
            else:
                min_val = min(a[i], b[j], c[k])
                if a[i] == min_val:
                    i += 1
                elif b[j] == min_val:
                    j += 1
                else:
                    k += 1
        return result


print(Solution.find_common( [1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120]))
print(Solution.find_common([1, 2, 3, 4, 5], [6, 7], [8, 9, 10]))
print(Solution.find_common([1, 1, 1, 2, 2, 2], [1, 1, 2, 2, 2], [1, 1, 1, 1, 2, 2, 2, 2]))
