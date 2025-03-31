# Problem link - https://www.geeksforgeeks.org/problems/count-squares3649/1


def count_squares(n):
    """
        Time complexity is O(log(n)) and space complexity is O(1).
    """

    # define a search space from 1 to n (n may or may not be a perfect square)
    low = 1
    high = n

    # typical binary search algorithm
    while low <= high:
        mid = int(low + (high - low)/2)

        # if the square of mid == n, then there would be exactly mid - 1 perfect squares
        # before n.
        if mid*mid == n:
            return mid - 1

        # else if square of mid is less than n, we must increase low to get closer to n.
        elif mid*mid < n:
            low = mid + 1

        # else we must decrement high to come closer to n.
        else:
            high = mid - 1

    # finally, high would point to the number of perfect squares less than n.
    return high


print(count_squares(9))
print(count_squares(3))
print(count_squares(27))
print(count_squares(67))
print(count_squares(36))