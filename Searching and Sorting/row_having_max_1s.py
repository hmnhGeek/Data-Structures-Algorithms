# Problem link - https://www.naukri.com/code360/problems/row-with-maximum-1-s_1112656

def get_1_count(row):
    # time complexity is O(log(m)) and O(1) space.
    low = 0
    high = len(row) - 1

    # typical binary search
    while low <= high:
        mid = int(low + (high - low) / 2)

        # if mid-element is 1, there could be more 1s at some lower indices.
        # so we reduce high to mid - 1.
        if row[mid] == 1:
            high = mid - 1
        else:
            # since mid-element is 0, we need to mover higher up to capture a 1.
            low = mid + 1

    # low represents the first index a 1 is encountered. Total number of 1s = length - low
    return len(row) - low


def get_max_1_row(mtx):
    # Overall time complexity is O(n*log(m)) and O(1) space.

    n, m = len(mtx), len(mtx[0])
    max_count = float('-inf')
    answer = None

    # this will take O(n) time for running the loop & O(log(m)) time to capture the counts of 1.
    for row in range(n):
        one_count = get_1_count(mtx[row])

        if one_count > max_count:
            max_count = one_count
            answer = row

    return answer


print(
    get_max_1_row(
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 0]
        ]
    )
)

print(
    get_max_1_row(
        [
            [1, 1],
            [1, 1]
        ]
    )
)

print(
    get_max_1_row(
        [
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1]
        ]
    )
)
