# Problem link - https://www.naukri.com/code360/problems/k-th-element-of-2-sorted-array_1164159
# Solution - https://www.youtube.com/watch?v=D1oDwWCq50g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=24

def get_kth(a1, a2, k):
    # This code is similar to the code of median in two sorted arrays. In that question,
    # we had to manually calculate how many elements lie on the left part, but here, since
    # we want kth element, we can say, left part will have k elements.
    n = len(a1) + len(a2)

    # if k is more than the length of the combined list, then return -1.
    if k > n:
        return -1

    short = min(a1, a2, key=len)
    large = a1 if short == a2 else a2

    low = 0
    high = k

    while low <= high:
        mid1 = int(low + (high - low)/2)
        mid2 = k - mid1

        l1 = short[mid1 - 1] if mid1 > 0 else float('-inf')
        l2 = large[mid2 - 1] if mid2 > 0 else float('-inf')
        r1 = short[mid1] if mid1 < len(short) else float('inf')
        r2 = large[mid2] if mid2 < len(large) else float('inf')

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)

        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1

print(
    get_kth(
        [2, 3, 45],
        [4, 6, 7, 8],
        4
    )
)

print(
    get_kth(
        [2, 3, 6, 7, 9],
        [1, 4, 8, 10],
        4
    )
)

print(
    get_kth(
        [1, 2, 3, 5, 6],
        [4, 7, 8, 9, 100],
        6
    )
)

print(
    get_kth(
        [1, 3, 6, 9, 10, 15],
        [8, 7, 15, 30, 40],
        11
    )
)

print(
    get_kth(
        [1, 2, 3],
        [2, 5, 7],
        6
    )
)