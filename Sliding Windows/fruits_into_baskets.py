def get_max_fruits_into_basket(fruit_categories):
    num_trees = len(fruit_categories)
    left = right = 0
    last_tree_for_fruits = dict()
    num_fruits_used = dict()
    baskets = set()
    max_fruits_collected = 1

    for fruit in fruit_categories:
        last_tree_for_fruits[fruit] = None
        num_fruits_used[fruit] = 0

    while right < num_trees:
        fruit = fruit_categories[right]
        last_tree_for_fruits[fruit] = right
        num_fruits_used[fruit] += 1
        baskets.add(fruit)

        if len(baskets) > 2:
            fruit_to_remove = fruit_categories[left]
            left = last_tree_for_fruits[fruit_to_remove] + 1
            num_fruits_used[fruit_to_remove] = 0
            baskets.remove(fruit_to_remove)

        max_fruits_collected = max(max_fruits_collected, right - left + 1)
        right += 1

    return max_fruits_collected


print(get_max_fruits_into_basket([1, 2, 1]))
print(get_max_fruits_into_basket([0, 1, 2, 2]))
print(get_max_fruits_into_basket([1, 2, 3, 2, 2]))
print(get_max_fruits_into_basket([3, 1, 2, 2, 2, 2]))
print(get_max_fruits_into_basket([1, 1, 2, 3]))
print(get_max_fruits_into_basket([1, 2, 3, 4]))
print(get_max_fruits_into_basket([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
