# Problem link - https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
# Solution - https://www.youtube.com/watch?v=tp8JIuCXBaU


def sort(arr):
    """
        Overall time complexity is O(n) and space complexity is O(1).
    """

    # initialize low, mid and high pointers
    low, mid, high = 0, 0, len(arr) - 1

    # The idea is that all elements from 0 to low - 1 will be 0s.
    # All elements from mid to high - 1 will be 1s.
    # All elements from high till end will be 2s.

    # run a loop till mid <= high...
    while mid <= high:
        # if a 0 is encountered at mid.
        if arr[mid] == 0:
            # swap with low and increment both mid and low.
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # if mid-element is 1, then simply increment mid.
            mid += 1
        else:
            # swap mid and high element and decrement only high; don't change mid.
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


a = [0, 1, 2, 0, 1, 2]
sort(a)
print(a)

b = [2, 1, 2, 0, 1, 2]
sort(b)
print(b)

c = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort(c)
print(c)

d = [0, 1, 0]
sort(d)
print(d)

e = [1, 1, 2, 2, 1]
sort(e)
print(e)