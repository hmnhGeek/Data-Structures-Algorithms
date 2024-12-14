class Solution:
    @staticmethod
    def common_in_arrays(left, mid, right):
        i, j, k = 0, 0, 0
        result = []
        while i < len(left) and j < len(mid) and k < len(right):
            if left[i] == mid[j] == right[k]:
                if left[i] not in result:
                    result.append(left[i])
                i += 1
                j += 1
                k += 1
            elif left[i] <= mid[j] and left[i] <= right[k]:
                i += 1
            elif mid[j] <= left[i] and mid[j] <= right[k]:
                j += 1
            else:
                k += 1
        return result


print(
    Solution.common_in_arrays(
        [1, 5, 10, 20, 40, 80],
        [6, 7, 20, 80, 100],
        [3, 4, 15, 20, 30, 70, 80, 120]
    )
)

print(
    Solution.common_in_arrays(
        [1, 2, 3, 4, 5],
        [6, 7],
        [8, 9, 10]
    )
)

print(
    Solution.common_in_arrays(
        [1, 1, 1, 2, 2, 2],
        [1, 1, 2, 2, 2],
        [1, 1, 1, 1, 2, 2, 2, 2]
    )
)

print(
    Solution.common_in_arrays(
        [1, 5, 10, 20, 30],
        [5, 13, 15, 20],
        [5, 20]
    )
)

print(
    Solution.common_in_arrays(
        [2, 5, 10, 30],
        [5, 20, 34],
        [5, 13, 19]
    )
)
