# Problem link - https://www.naukri.com/code360/problems/4sum_5713771
# Solution - https://www.youtube.com/watch?v=eD95WRfh81c


class Solution:
    @staticmethod
    def four_sum(arr: list, target):
        """
            Time complexity is O(n^3 + nlog(n)) and space complexity is O(1).
        """

        copy = arr.copy()
        copy.sort()
        n = len(copy)
        result = []
        for i in range(n):
            if i > 0 and copy[i] == copy[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and copy[j] == copy[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    _sum = copy[i] + copy[j] + copy[k] + copy[l]
                    if _sum == target:
                        result.append([copy[i], copy[j], copy[k], copy[l]])
                        k += 1
                        l -= 1
                        while k < l and copy[k] == copy[k - 1]:
                            k += 1
                        while k < l and copy[l] == copy[l + 1]:
                            l -= 1
                    elif _sum < target:
                        k += 1
                    else:
                        l -= 1
        return result


print(Solution.four_sum([2, 2, 2, 2, 1, 3], 8))
print(Solution.four_sum([1, 1, 1, 0], 4))
print(Solution.four_sum([1, 0, -1, 0, -2, 2], 0))
print(Solution.four_sum([2, 2, 2, 2, 2], 8))
