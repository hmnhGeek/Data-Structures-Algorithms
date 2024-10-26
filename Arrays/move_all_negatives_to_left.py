def move(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] >= 0 and arr[j] >= 0:
            j -= 1
        elif arr[i] >= 0 and arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] < 0 and arr[j] >= 0:
            i += 1
            j -= 1
        else:
            i += 1
    print(arr)


move([-12, 11, -13, -5, 6, -7, 5, -3, -6])
move([-1, 2, -3, 4, 5, 6, -7, 8, 9])
move([-12, 11, -13, -5, 6, -7, 5, -3, 11])
move([1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1])