# Problem link - https://www.naukri.com/code360/problems/search-in-a-rotated-sorted-array-ii_7449547

def search(arr, target):
    '''
        Overall time complexity is O(log(n)) and space is O(1).

        However, in some cases it could happen that you might have to shrink
        continuously till the middle part (maybe when almost all the elements
        are the same). In that case, you would traverse n/2 times. In that
        worst case, the time complexity becomes O(n).
    '''
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        if arr[mid] == target:
            return True

        if arr[low] == arr[mid] == arr[high]:
            # if low, mid and high point to same value,
            # then you cannot identify left or right
            # sorted parts. So when this happens, shrink
            # the search space, i.e., increase the low
            # and decrease the high at the same time.
            # Also ensure that you continue, because
            # it's not confirmed that even after shrinking
            # will the low, mid and high point to different
            # values.
            low += 1
            high -= 1
            continue

        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


print(search([3, 4, 5, 0, 0, 1, 2], 4))
print(search([31, 44, 56, 0, 10, 13], 47))
print(search([3, 1, 3, 3, 3, 3], 1))