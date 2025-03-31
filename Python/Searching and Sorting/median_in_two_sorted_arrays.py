# Problem link - https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Solution - https://www.youtube.com/watch?v=C2rRzz-JDk8&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=22

def median(arr1, arr2):
    # This will take O(n) time and O(1) space.

    n = len(arr1) + len(arr2)
    # counter will keep track of the index from the virtually merged array
    counter = 0
    i, j = 0, 0

    # be n even or odd, in both cases, idx2 and elem2 will be needed.
    # only in even case, idx1 and elem1 will be used.
    idx1, idx2 = n//2 - 1, n//2
    elem1, elem2 = -1, -1

    # typical merge approach for merging two sorted arrays.
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            # if counter is equivalent to any of the indices idx1 or idx2,
            # because arr1[i] <= arr2[j], assign elem1 or elem2 to arr1[i].
            # increment counter and i.
            if counter == idx1:
                elem1 = arr1[i]
            elif counter == idx2:
                elem2 = arr1[i]
            counter += 1
            i += 1
        else:
            # if counter is equivalent to any of the indices idx1 or idx2,
            # because arr1[i] > arr2[j], assign elem1 or elem2 to arr2[j].
            # increment counter and j.
            if counter == idx1:
                elem1 = arr2[j]
            elif counter == idx2:
                elem2 = arr2[j]
            counter += 1
            j += 1

    # if counter is equivalent to any of the indices idx1 or idx2,
    # assign elem1 or elem2 to arr1[i] increment counter and i.
    while i < len(arr1):
        if counter == idx1:
            elem1 = arr1[i]
        elif counter == idx2:
            elem2 = arr1[i]
        counter += 1
        i += 1

    # if counter is equivalent to any of the indices idx1 or idx2,
    # assign elem1 or elem2 to arr2[j] increment counter and j.
    while j < len(arr2):
        if counter == idx1:
            elem1 = arr2[j]
        elif counter == idx2:
            elem2 = arr2[j]
        counter += 1
        j += 1

    # finally, if the merged virtual array has even-number of elements,
    # return (elem1 + elem2)/2, else simply return elem2.
    if n % 2 == 0:
        return (elem1 + elem2)/2
    return elem2


print(median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(median([1, 3, 4], [2, 3]))