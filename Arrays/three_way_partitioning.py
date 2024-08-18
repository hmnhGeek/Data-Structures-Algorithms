def partition(arr, range_interval):
    """
        The idea is to divide the array into 4 parts:
        1. All values smaller than low.
        2. All values equal to low value should be counted.
        3. All values within range will be stored in a separate array.
        4. All values equal to high will be counted.
        5. All values greater than high should be in a third array

        Overall, we take O(N) time and O(N) space.
    """

    low, high = range_interval[0], range_interval[1]

    # exception case
    if low > high:
        return

    lesser, low_count, between, high_count, highers = [], 0, [], 0, []

    # populate the 3 arrays and also keep a track of count of elements from the array which are
    # equal to the range limit values. This takes O(N) time and O(N) space.
    for elem in arr:
        if elem == low:
            low_count += 1
        elif elem == high:
            high_count += 1
        elif elem < low:
            lesser.append(elem)
        elif low < elem < high:
            between.append(elem)
        elif high < elem:
            highers.append(elem)

    # Start populating the original array back in O(N) time.

    # start modifying original array from lesser elements first
    i = 0
    for j in range(len(lesser)):
        arr[i] = lesser[j]
        i += 1

    # modify index in array until low count becomes 0, i.e., add low values to array if any.
    while low_count != 0:
        arr[i] = low
        i += 1
        low_count -= 1

    # now add the middle elements
    for j in range(len(between)):
        arr[i] = between[j]
        i += 1

    # modify index in array until high count becomes 0, i.e., add high values to array if any.
    while high_count != 0:
        arr[i] = high
        i += 1
        high_count -= 1

    # finally, add the higher elements
    for j in range(len(highers)):
        arr[i] = highers[j]
        i += 1


arr1 = [5, 7, 1, 4, 6, 3]
partition(arr1, [2, 4])
print(arr1)

arr2 = [1, 4, 3, 6, 2, 1]
partition(arr2, [1, 3])
print(arr2)

arr3 = [1, 2, 3, 3, 4]
partition(arr3, [1, 2])
print(arr3)

arr4 = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
partition(arr4, [14, 20])
print(arr4)

arr5 = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
partition(arr5, [20, 20])
print(arr5)