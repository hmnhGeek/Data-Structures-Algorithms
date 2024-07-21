from math import log10
from math import floor


def log5(x): return log10(x)/log10(5)


def number_of_trailing_zeroes(n):
    '''
        Overall time complexity is O(log5(n)) and
        Overall space complexity is O(1)
    '''

    # takes O(1) time
    num_terms = log5(n)

    # takes O(1) time
    num_denom = floor(num_terms)

    # takes O(log5(n)) time because the loop runs num_denom times
    result = 0
    for i in range(1, num_denom + 1):
        result += floor(n/5**i)

    return result


def get_num_from_trail(z, show_comments = False):
    '''
        Overall time complexity is O(log2(n) * log5(n))
        Overall space complexity is O(1).
    '''

    if z == 0: return 0

    low = 1
    high = 10**4

    # This is classical binary search, which takes O(log2(n)) time
    while low <= high:
        mid = (low + high) // 2

        # this takes O(log5(n)) time.
        num_trail = number_of_trailing_zeroes(mid)
        if show_comments:
            print(f"For mid = {mid}, got {num_trail}, required = {z}, low = {low}, high = {high}")

        if num_trail < z:
            if show_comments:
                print(f"We must check for large numbers to add more zeroes, therefore, increasing low from {low} to {mid + 1}")
            low = mid + 1
        else:
            if show_comments:
                if num_trail == z:
                    print(f'''We got required number of zeroes. But question asked for the least number. We can have a lower 
                    number with same (i.e. required) number of 0s. Therefore check for lower numbers once.''')
                else:
                    print("We got more zeros. We must decrease high.")
                print(f"Decreasing high from {high} to {mid - 1}")
            high = mid - 1

        if show_comments:
            print()

    return low


print(get_num_from_trail(6))
print(get_num_from_trail(1))
print(get_num_from_trail(0))
print(get_num_from_trail(100, show_comments=True))
