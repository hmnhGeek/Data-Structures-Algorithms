def get_max_points_from_cards(cards_with_points, deck_size):
    number_of_cards = len(cards_with_points)
    if deck_size > number_of_cards:
        return

    left, right = 0, deck_size - 1
    max_points_obtained = sum(cards_with_points[left:right + 1])
    deck_sum = max_points_obtained
    while left != (number_of_cards - deck_size) and right != number_of_cards - 1:
        deck_sum -= cards_with_points[right]
        right -= 1
        if right < 0:
            right = number_of_cards - 1

        left -= 1
        if left < 0:
            left = number_of_cards - 1
        deck_sum += cards_with_points[left]
        max_points_obtained = max(max_points_obtained, deck_sum)
    return max_points_obtained


print(get_max_points_from_cards([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(get_max_points_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(get_max_points_from_cards([2, 2, 2], 2))
print(get_max_points_from_cards([9, 7, 7, 9, 7, 7, 9], 7))
print(get_max_points_from_cards([9, 7, 5, 3, 2, 1, 8], 4))
print(get_max_points_from_cards([8, 7, 5, 3, 2], 3))
print(get_max_points_from_cards([5, 4, 9, 7, 8], 5))
