def root(n):
    # Time complexity is O(log(n)) and space is O(1).
    if n < 0:
        return
    low, high = 0, n

    while low <= high:
        mid = int(low + (high - low)/2)

        if mid*mid == n:
            return mid

        if mid*mid < n:
            low = mid + 1
        else:
            high = mid - 1

    return low - 1


print(root(26))
print(root(87))
print(root(99))
print(root(924))
print(root(0))
print(root(1))
print(root(2))