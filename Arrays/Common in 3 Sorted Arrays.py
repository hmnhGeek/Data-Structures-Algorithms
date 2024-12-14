# Problem link - https://www.geeksforgeeks.org/problems/common-elements1132/1


class Solution:
    @staticmethod
    def common_in_arrays(left, mid, right):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # define three pointers to track the three arrays.
        i, j, k = 0, 0, 0
        # define a result list which will store the common elements.
        result = []
        # while all three lists have to be traversed...
        while i < len(left) and j < len(mid) and k < len(right):
            # if all the three elements match and the common element is not in result, add it.
            if left[i] == mid[j] == right[k]:
                if left[i] not in result:
                    result.append(left[i])
                # increment the three pointers simultaneously.
                i += 1
                j += 1
                k += 1
            # else, increment the minimum pointer.
            elif left[i] <= mid[j] and left[i] <= right[k]:
                i += 1
            elif mid[j] <= left[i] and mid[j] <= right[k]:
                j += 1
            else:
                k += 1
        # return the result list.
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

print(
    Solution.common_in_arrays(
        [2, 3, 4, 7],
        [0, 0, 3, 5],
        [1, 3, 8, 9]
    )
)
