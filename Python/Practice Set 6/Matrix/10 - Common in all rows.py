# Problem link - https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/


from collections import Counter


class Solution:
    @staticmethod
    def find_common_in_all_rows(mtx):
        """
            Time complexity is O(nm) and space complexity is O(m).
        """

        n, m = len(mtx), len(mtx[0])

        # this dictionary will contain the common elements (with count) up until each row traversed.
        tracking_dict = dict(Counter(mtx[0]))

        # start from the second row
        for i in range(1, n):

            # this dictionary will be used in each loop to hold common elements till that row.
            temp = dict()

            # loop through the elements of the row
            for j in range(m):
                elem = mtx[i][j]

                # if the element is present in the tracking dictionary, then decrease its count first of all...
                if elem in tracking_dict and tracking_dict[elem] > 0:
                    tracking_dict[elem] -= 1

                    # add it in temp
                    if elem not in temp:
                        temp[elem] = 1
                    else:
                        temp[elem] += 1

            # update the common elements
            tracking_dict = temp

        # now populate the common elements in a list using the frequencies.
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
