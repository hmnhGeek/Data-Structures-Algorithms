# Problem link - https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
# Solution - https://www.youtube.com/watch?v=nP_ns3uSh80


def find_majority_element(arr):
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    n = len(arr)
    elem, count = None, 0

    # this will take O(n) time
    for i in range(len(arr)):
        # if the count value is 0, a new element shall be checked
        if count == 0:
            # update the element to the ith element of the array
            elem = arr[i]
            # increment the count
            count += 1
        elif arr[i] == elem:
            # if count was not 0, and the ith element is same as stored element,
            # increase the count value
            count += 1
        else:
            # if the count was not 0 and the ith element do not match, decrement the count
            count -= 1

    # finally, we will have an element which COULD be a possible majority element.
    # reset count to 0 to count the number of times this stored element occurs in the array.
    count = 0

    # an additional O(n) time.
    for i in range(len(arr)):
        if arr[i] == elem:
            count += 1

    # return the element if the count is > n/2 else return -1.
    return elem if count > n // 2 else -1


print(find_majority_element([3, 1, 3, 3, 2]))
print(find_majority_element([7]))
print(find_majority_element([2, 13]))
print(find_majority_element([3, 2, 3]))
print(find_majority_element([2, 2, 1, 1, 1, 2, 2]))
