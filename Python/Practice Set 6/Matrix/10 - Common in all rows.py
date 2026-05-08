from collections import Counter


class Solution:
    @staticmethod
    def find_common_in_all_rows(mtx):
        n, m = len(mtx), len(mtx[0])
        temp = dict()
        tracking_dict = dict(Counter(mtx[0]))
        for i in range(1, n):
            for j in range(m):
                elem = mtx[i][j]
                if elem in tracking_dict and tracking_dict[elem] > 0:
                    tracking_dict[elem] -= 1
                    if elem not in temp:
                        temp[elem] = 1
                    else:
                        temp[elem] += 1
            tracking_dict = temp
        common_elements = []
        for k in tracking_dict:
            for _ in range(tracking_dict[k]):
                common_elements.append(k)
        return common_elements


print(
    Solution.find_common_in_all_rows(
        [
            [1, 2, 1, 4, 8],
            [3, 7, 8, 5, 1],
            [8, 7, 7, 3, 1],
            [8, 1, 2, 7, 9]
        ]
    )
)
