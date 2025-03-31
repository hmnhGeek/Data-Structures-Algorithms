# Problem link - https://www.naukri.com/code360/problems/unique-element-in-sorted-array_1112654

def is_mid_single(arr, mid):
    # if mid is not the first or last element
    if mid in range(1, len(arr) - 1):
        return arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]

    # if mid is 0th index, check for only the next index
    if mid == 0:
        return arr[mid] != arr[mid + 1]

    # now mid could only be last index, check from second last element only.
    return arr[mid - 1] != arr[mid]


def get_single_element(arr):
    '''
        Typical binary search. Takes O(log(n)) time and O(1) space.
    '''

    # if there is only one element in the array, then it's the only single element
    # return it
    if len(arr) == 1:
        return arr[0]

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        # if the mid element is single, return it.
        if is_mid_single(arr, mid):
            return arr[mid]

        if arr[mid + 1] == arr[mid]:
            if (high - mid - 1) % 2 == 0:
                # right side has even elements post the duplicate one,
                # hence move to the left side.
                high = mid - 1
            else:
                # since the mid + 1 is same as mid, and post mid + 1, we
                # have odd number of elements, the single element must
                # lie on the right side.
                low = mid + 2
        else:
            if (mid - low - 1) % 2 == 0:
                # since the mid - 1 is same as mid, and before mid - 1,
                # we have even number of elements, so move right.
                low = mid + 1
            else:
                # else if mid - 2 has odd number of elements, then the
                # single element must be on the left side.
                high = mid - 2

    return -1


print(get_single_element([1, 1, 2, 2, 4, 5, 5]))
print(get_single_element([1, 1, 3, 5, 5]))
print(get_single_element([1, 1, 4, 4, 15]))
print(get_single_element([1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]))
print(get_single_element([1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]))
print(get_single_element([1, 2, 2]))
print(get_single_element([1, 1, 2]))
print(get_single_element([]))
print(get_single_element([1, 1, 2, 2, 3, 3, 15, 15]))
print(get_single_element([-4, -4, -2, 0, 0, 15, 15]))
print(get_single_element([5]))
