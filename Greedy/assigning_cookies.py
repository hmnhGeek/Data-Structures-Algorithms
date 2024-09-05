def get_num_assigned_cookies(cookie_sizes, greed_factors):
    cookie_sizes.sort()
    greed_factors.sort()

    left, right = 0, 0
    while left < len(cookie_sizes) and right < len(greed_factors):
        if cookie_sizes[left] >= greed_factors[right]:
            right += 1
        left += 1
    return right

print(get_num_assigned_cookies([4, 2, 1, 2, 1, 3], [1, 5, 3, 3, 4]))
print(get_num_assigned_cookies([1, 1], [1, 2, 3]))
print(get_num_assigned_cookies([1, 2, 3], [1, 1]))