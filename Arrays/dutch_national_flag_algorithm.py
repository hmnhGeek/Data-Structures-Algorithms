def sort(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
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