# Problem link - https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Solution - https://www.youtube.com/watch?v=F9c7LpRZWVQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=23

def find_median(a1, a2):
    # The time complexity would be O(n + log(len(short))). n is coming because we take
    # an average a linear time to determine the shorter length array out of a1 and a2.

    # Space complexity is O(1) because to store shorter and larger arrays we just use
    # references in python.

    # store the combined length of the arrays. This will be useful in deciding approaches
    # for handling median in odd and even number of elements.
    n = len(a1) + len(a2)

    # get the shorter and larger arrays out of a1 and a2. The approach is to pick x elements
    # from a1 and (n - x) elements from a2 (when n is even) or ({n + 1}/2 - x) from a2 (when
    # n is odd) to determine the median.
    short = min(a1, a2, key=len)
    large = a2 if a1 == short else a1

    low = 0
    high = len(short)

    while low <= high:
        # mid1 denotes the index from shorter array. mid1 is such an index that we pick
        # elements from shorter array till index mid1 - 1 (inclusive). Basically, we will
        # pick mid1 number of elements from short array (as indexing starts from 0).
        mid1 = int(low + (high - low)/2)

        # rest mid2 number of elements will be picked from larger array. Irrespective
        # of n being even or odd, (n+1)//2 will always return total number of elements
        # required on left side. Say, if n = 10, then 11/2 = 5 (5 on left and 5 on right).
        # If n = 9, 10//2 = 5. Hence we just have to decide how many to keep on left.
        mid2 = (n + 1)//2 - mid1

        # we create 4 numbers
        # l1 is the maximum picked from shorter array on the left side
        # l2 is the maximum picked from the larger array on the left side
        # r1 is the minimum picked from the shorter array on the right side
        # r2 is the minimum picked from the larger array on the right side.
        l1 = short[mid1 - 1] if mid1 > 0 else float('-inf')
        l2 = large[mid2 - 1] if mid2 > 0 else float('-inf')
        r1 = short[mid1] if mid1 < len(short) else float('inf')
        r2 = large[mid2] if mid2 < len(large) else float('inf')

        # if the numbers satisfy this cross relation, then it means that
        # in whole, the combined list is in sorted order. And if now, n
        # is even, return the average of (max from left + min from right)/2
        # else in odd case simply return max from left.
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 0:
                return (max(l1, l2) + min(r1, r2))/2
            else:
                return max(l1, l2)

        # if l1 > r2, basically we included more elements on the left side,
        # let's decrease the number of elements on the left side coming from
        # the shorter array and increase them from the larger array.
        elif l1 > r2:
            high = mid1 - 1
        else:
            # opposite of the above scenario
            low = mid1 + 1

print(
    find_median(
        [2, 4],
        [1, 3, 4]
    )
)

print(
    find_median(
        [1, 3, 4, 7, 10, 12],
        [2, 3, 6, 15]
    )
)

print(
    find_median(
        [1, 9, 16, 20, 21, 30],
        [25, 35]
    )
)