def count_squares(n):
    low = 1
    high = n
    while low <= high:
        mid = int(low + (high - low)/2)
        if mid*mid == n:
            return mid - 1
        elif mid*mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return high


print(count_squares(9))
print(count_squares(3))
print(count_squares(27))
print(count_squares(67))
print(count_squares(36))