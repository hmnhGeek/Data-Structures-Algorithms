def get_max_consecutive_ones_with_k_zeros(array, k):
    max_size_recorded = 1
    left = right = 0
    num_zeroes_used = 0
    num_elements = len(array)

    while right < num_elements:
        if array[right] == 1:
            max_size_recorded = max(max_size_recorded, right - left + 1)
            right += 1
        else:
            num_zeroes_used += 1
            if num_zeroes_used <= k:
                max_size_recorded = max(max_size_recorded, right - left + 1)
            else:
                while num_zeroes_used > k:
                    left += 1
                    if array[left - 1] == 0:
                        num_zeroes_used -= 1
                max_size_recorded = max(max_size_recorded, right - left + 1)
            right += 1

    return max_size_recorded


print(get_max_consecutive_ones_with_k_zeros([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(get_max_consecutive_ones_with_k_zeros([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(get_max_consecutive_ones_with_k_zeros([0, 1, 1, 0, 1, 0, 1, 1], 2))