# Problem link - https://leetcode.com/problems/assign-cookies/
# Solution - https://www.youtube.com/watch?v=DIX2p7vb9co&list=PLgUwDviBIf0rF1w2Koyh78zafB0cz7tea&index=1


def get_num_assigned_cookies(cookie_sizes, greed_factors):
    """
        Overall time complexity is O(nlog(n) + mlog(m) + n + m) and overall space complexity is O(1).
    """

    # first sort both then arrays in O(nlog(n) + mlog(m)) time.
    cookie_sizes.sort()
    greed_factors.sort()

    # start a two pointer approach; till the pointers are within limits; O(n + m)
    left, right = 0, 0
    while left < len(cookie_sizes) and right < len(greed_factors):
        # if the current cookie has a size more than the greed factor of the current child,
        # then move to the next child (assuming the current cookie to be assigned to him/her).
        if cookie_sizes[left] >= greed_factors[right]:
            right += 1

        # by default, move to the next cookie
        left += 1

    # return the index of the "not yet assigned child" which would be the count of the number
    # of children having the cookies assigned (0 based indexing).
    return right


print(get_num_assigned_cookies([4, 2, 1, 2, 1, 3], [1, 5, 3, 3, 4]))
print(get_num_assigned_cookies([1, 1], [1, 2, 3]))
print(get_num_assigned_cookies([1, 2, 3], [1, 1]))