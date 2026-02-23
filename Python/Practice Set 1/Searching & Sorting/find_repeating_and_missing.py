class Solution:
    @staticmethod
    def find_repeating_and_missing(arr):
        n = len(arr)
        sum_of_n_natural_numbers = n*(n + 1)/2
        sum_sq_of_n_natural_numbers = n * (n + 1) * (2*n + 1)/6
        sum_of_array = sum(arr)
        sum_sq_of_array = sum(i**2 for i in arr)
        repeating_number = 0.5 * (sum_of_array - sum_of_n_natural_numbers + ((sum_sq_of_array - sum_sq_of_n_natural_numbers)/(sum_of_array - sum_of_n_natural_numbers)))
        missing_number = repeating_number - sum_of_array + sum_of_n_natural_numbers
        return repeating_number, missing_number


print(Solution.find_repeating_and_missing([2, 2]))
print(Solution.find_repeating_and_missing([1, 3, 3]))
print(Solution.find_repeating_and_missing([4, 3, 6, 2, 1, 1]))
