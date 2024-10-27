from typing import List


class MissingAndRepeatingDTO:
    def __init__(self, missing, repeating):
        self.missing = missing
        self.repeating = repeating

    def __str__(self):
        return f"Missing: {self.missing}, Repeating: {self.repeating}"

def find_missing_and_repeating(arr: List[int]) -> MissingAndRepeatingDTO:
    n = len(arr)
    s, sq_s = 0, 0
    sn = n*(n + 1)/2
    sn2 = n*(n + 1)*(2*n + 1)/6

    for i in range(n):
        s += arr[i]
        sq_s += arr[i]**2

    # repeating - missing = S - Sn
    repeating_minus_missing = s - sn

    # repeating ith squares sum - missing ith squares sum = (repeating - missing)(repeating + missing) = v
    repeating_minus_missing_ith_squares = (sq_s - sn2)/repeating_minus_missing

    repeating = (repeating_minus_missing + repeating_minus_missing_ith_squares)/2
    missing = repeating_minus_missing_ith_squares - repeating
    dto = MissingAndRepeatingDTO(missing, repeating)
    return dto


print(find_missing_and_repeating([2, 2]))
print(find_missing_and_repeating([1, 3, 3]))
print(find_missing_and_repeating([4, 3, 6, 2, 1, 1]))