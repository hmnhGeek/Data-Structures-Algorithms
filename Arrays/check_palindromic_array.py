# Problem link - https://www.geeksforgeeks.org/problems/palindromic-array-1587115620/1


def is_palindrome(string):
    return string == string[-1:-len(string)-1:-1]


def is_palindromic_array(arr):
    for i in arr:
        if not is_palindrome(str(i)):
            return False
    return True


print(is_palindromic_array([111, 222, 333, 444, 555]))
print(is_palindromic_array([21, 131, 20]))