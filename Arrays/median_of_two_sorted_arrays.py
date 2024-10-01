# Problem link - https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Solution - https://www.youtube.com/watch?v=F9c7LpRZWVQ


def find_median(arr1, arr2):
    # Overall time complexity is O(log(min(len(a1), len(a2)))) and space complexity is O(1).
    n1 = len(arr1)
    n2 = len(arr2)

    # we will run the while loop of the binary search on the smaller array to avoid TLE.
    if n1 > n2:
        return find_median(arr2, arr1)

    # define the search space
    low, high = 0, n1

    # left_count denotes the number of elements on the left of the median. In both even and odd cases,
    # we want consistent left_count, and hence (n + 1)//2.
    n = n1 + n2
    left_count = (n + 1) // 2

    # Typical binary search
    while low <= high:
        # mid1 denotes the index from arr1 which falls in the right section of the median
        mid1 = int(low + (high - low) / 2)
        # mid2 denotes the index from arr2 which falls in the right section of the median.
        mid2 = left_count - mid1

        # compute l1, l2, r1 and r2.
        l1 = arr1[mid1 - 1] if mid1 - 1 >= 0 else float('-inf')
        l2 = arr2[mid2 - 1] if mid2 - 1 >= 0 else float('-inf')
        r1 = arr1[mid1] if mid1 < n1 else float('inf')
        r2 = arr2[mid2] if mid2 < n2 else float('inf')

        # if median condition is satisfied, return the median
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            return (max(l1, l2) + min(r1, r2)) / 2
        elif l1 > r2:
            # if l1 > r2, reduce high
            high = mid1 - 1
        else:
            # else increase low
            low = mid1 + 1

    # this shall never execute
    return 0


print(find_median([2, 3, 5, 8], [10, 12, 14, 16, 18, 20]))
print(find_median([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(find_median([], [2, 4, 5, 6]))
print(find_median([1, 3], [2]))
print(find_median([1, 2], [3, 4]))
