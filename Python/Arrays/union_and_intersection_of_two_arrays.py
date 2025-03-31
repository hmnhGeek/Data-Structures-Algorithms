# Problem link - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1


from typing import List


def union(arr1: List[int], arr2: List[int]) -> set:
    """
        Overall time complexity is O(n + m) and overall space complexity is O(n + m).
    """

    union_set = set()

    # This will take O(n) time.
    for i in arr1:
        union_set.add(i)

    # This will take O(m) time.
    for i in arr2:
        union_set.add(i)

    # The set will take O(n + m) space in worst case.
    return union_set


def intersection(arr1: List[int], arr2: List[int]) -> set:
    """
        Overall time complexity is O(m + n) and overall space complexity is O(m + n).
    """

    l1_set = set()
    intersection_set = set()

    # This will take O(n) time.
    for i in arr1:
        l1_set.add(i)

    # This will take O(m) time.
    for i in arr2:
        # lookup is amortized O(1).
        if i in l1_set:
            intersection_set.add(i)

    # The intersection will hold O(n + m) space in worst case.
    return intersection_set


print(union([1, 2, 3, 4, 5], [1, 2, 3]))
print(intersection([1, 2, 3, 4, 5], [1, 2, 3]))
print(union([85, 25, 1, 32, 54, 6], [85, 2]))
print(intersection([85, 25, 1, 32, 54, 6], [85, 2]))
print(union([1, 2, 1, 1, 2], [2, 2, 1, 2, 1]))
print(intersection([1, 2, 1, 1, 2], [2, 2, 1, 2, 1]))
