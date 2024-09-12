def get_max_points_from_cards(cards_with_points, deck_size):
    """
        Time complexity is O(k) and space complexity is O(1).
        :param cards_with_points: An array of integers denoting the points that each card holds.
        :param deck_size: An integer value denoting the size of deck that needs to be picked up.
        :return: The maximum points that you can obtain from the deck size.
    """

    # store the number of cards.
    number_of_cards = len(cards_with_points)

    # if the required deck size is greater than the number of cards, then return
    if deck_size > number_of_cards:
        return

    # define the window.
    left, right = 0, deck_size - 1

    # store the sum of the window elements.
    max_points_obtained = sum(cards_with_points[left:right + 1])
    # create a copy which we will update on each iteration.
    deck_sum = max_points_obtained

    # since `k` sized deck can be picked from the front, or rear, or a contagious combination of
    # both ends, we will first start by picking all the k cards from front and then one by one
    # reduce cards from front and add from rear. This way, our loop ends when we have to pick
    # all the k cards from rear end, i.e., left becomes #cards - deck_size and right becomes the
    # last card.
    while left != (number_of_cards - deck_size) and right != number_of_cards - 1:
        # decrease the right card from the sum and reduce right pointer
        deck_sum -= cards_with_points[right]
        right -= 1
        # if right pointer has become negative, immediately restore it to the last index.
        if right < 0:
            right = number_of_cards - 1

        # now first reduce the left pointer and then add its value to the sum.
        left -= 1
        # if left pointer has become negative, immediately restore it to the last index.
        if left < 0:
            left = number_of_cards - 1
        # add it to sum.
        deck_sum += cards_with_points[left]

        # update the max_points_obtained sum
        max_points_obtained = max(max_points_obtained, deck_sum)

    # return max_points_obtained
    return max_points_obtained


print(get_max_points_from_cards([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
print(get_max_points_from_cards([1, 2, 3, 4, 5, 6, 1], 3))
print(get_max_points_from_cards([2, 2, 2], 2))
print(get_max_points_from_cards([9, 7, 7, 9, 7, 7, 9], 7))
print(get_max_points_from_cards([9, 7, 5, 3, 2, 1, 8], 4))
print(get_max_points_from_cards([8, 7, 5, 3, 2], 3))
print(get_max_points_from_cards([5, 4, 9, 7, 8], 5))
