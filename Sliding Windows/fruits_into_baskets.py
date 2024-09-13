def get_max_fruits_into_basket(fruit_categories):
    # store the number of trees for array traversal
    num_trees = len(fruit_categories)

    # initialize a window of size 1 from index 0 to index 0.
    left = right = 0

    # create a blank dictionary to store the last indices where any fruit was found
    last_tree_for_fruits = dict()

    # create a set denoting the baskets in which you will be storing the unique categories of fruits collected till now.
    baskets = set()

    # since the window size is 1, you say that the fruits collected are 1.
    max_fruits_collected = 1

    # for every fruit, set the last tree at which they are found to be None.
    for fruit in fruit_categories:
        last_tree_for_fruits[fruit] = None

    # traverse the trees
    while right < num_trees:
        # get the current fruit
        fruit = fruit_categories[right]

        # update the last tree at which it is found
        last_tree_for_fruits[fruit] = right

        # add the fruit to the basket
        baskets.add(fruit)

        # if there are more than 2 fruits (denoting a requirement of 3rd basket and so on), then we must remove some
        # fruits because we only have 2 baskets.
        if len(baskets) > 2:
            # start shrinking the window by removing the fruit from the left side.
            fruit_to_remove = fruit_categories[left]

            # since right must have travelled upon this fruit, it will be surely found in `last_tree_for_fruits`. Set
            # the left pointer to the next tree from `last_tree_for_fruits`, basically, we have removed all the fruits
            # of category `fruit_to_remove`.
            left = last_tree_for_fruits[fruit_to_remove] + 1

            # thus remove the fruit from basket as well
            baskets.remove(fruit_to_remove)

        # update the window size.
        max_fruits_collected = max(max_fruits_collected, right - left + 1)
        # increment the right pointer to consider the next fruit.
        right += 1

    # return the max fruits collected of two categories at most.
    return max_fruits_collected


print(get_max_fruits_into_basket([1, 2, 1]))
print(get_max_fruits_into_basket([0, 1, 2, 2]))
print(get_max_fruits_into_basket([1, 2, 3, 2, 2]))
print(get_max_fruits_into_basket([3, 1, 2, 2, 2, 2]))
print(get_max_fruits_into_basket([1, 1, 2, 3]))
print(get_max_fruits_into_basket([1, 2, 3, 4]))
print(get_max_fruits_into_basket([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
