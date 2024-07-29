# Problem link - https://www.naukri.com/code360/problems/find-peak-element_1081482
# Video solution - https://www.youtube.com/watch?v=cXxmbemS6XM&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=10

def get_peak_element(arr):
    '''
        Overall time complexity is O(log(n)) and space complexity is O(1).
    '''

    # try to avoid as much binary search as possible.
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)

    # handle the extreme left and extreme right separately so that
    # inside the binary search we don't have to worry about mid - 1
    # and mid + 1 index.
    if arr[0] > arr[1]:
        return arr[0]
    if arr[-1] > arr[-2]:
        return arr[-1]

    low, high = 1, len(arr) - 1
    while low <= high:
        mid = int(low + (high - low)/2)

        # if the mid-index is already a peak, return arr[mid]
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return arr[mid]

        # if we are on a monotonous increasing path, the peak will lie on the right part.
        # here we will not use arr[low] <= arr[mid] from previous questions because in
        # those questions, both lines before and after the discontinuity were monotonously
        # increasing. Here we have to find peak, in which there will be one increasing part
        # and the other decreasing part.
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            # it will handle the case of local minima as well.
            high = mid - 1


print(get_peak_element([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
print(get_peak_element([1, 8, 1, 5, 3]))
print(get_peak_element([1, 2, 1]))
print(get_peak_element([1, 2, 3]))
print(get_peak_element([]))
print(get_peak_element([1, 2, 3, 3, 5, 6, 6, 7, 8, 8, 5, 1]))
print(get_peak_element([3, 2, 1]))
print(get_peak_element([1, 10, 13, 7, 6, 5, 4, 2, 1, 0]))
print(get_peak_element([5, 4, 3, 2, 1, 0]))
print(get_peak_element([1, 2, 3, 4, 5, 6]))
print(get_peak_element([1, 5, 1, 2, 1]))