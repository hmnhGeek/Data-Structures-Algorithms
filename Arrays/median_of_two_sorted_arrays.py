def find_median(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 > n2:
        return find_median(arr2, arr1)

    low, high = 0, n1
    n = n1 + n2
    left_count = (n + 1)//2

    while low <= high:
        mid1 = int(low + (high - low)/2)
        mid2 = left_count - mid1
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        if mid1 < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        if mid1 - 1 >= 0:
            l1 = arr1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = arr2[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            return (max(l1, l2) + min(r1, r2))/2
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0


print(find_median([2, 3, 5, 8], [10, 12, 14, 16, 18, 20]))
print(find_median([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(find_median([], [2, 4, 5, 6]))
print(find_median([1, 3], [2]))
print(find_median([1, 2], [3, 4]))