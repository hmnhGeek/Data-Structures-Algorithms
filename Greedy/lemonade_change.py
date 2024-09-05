# Problem link - https://leetcode.com/problems/lemonade-change/description/
# Solution - https://www.youtube.com/watch?v=n_tmibEhO6Q&list=PLgUwDviBIf0rF1w2Koyh78zafB0cz7tea&index=2

def is_change_possible(denominations):
    # Time complexity is O(N) and space is O(1).

    # initially the stall has no denominations
    fives, tens, twenties = 0, 0, 0

    for denomination in denominations:
        if denomination == 5:
            # if customer pays in $5, increment denomination 5 count.
            fives += 1
        elif denomination == 10:
            # if customer pays in $10, increment denomination 10 count.
            # return back $5 else return False, if you don't have $5.
            tens += 1
            if fives > 0:
                fives -= 1
            else:
                return False
        else:
            # if customer pays in $20, return $15.

            # check if you have a $10 and a $5. The greedy aspect comes here as here
            # we are trying to greedily utilize $10 first because we might need $5 in most cases.
            if fives > 0 and tens > 0:
                fives -= 1
                tens -= 1
            # otherwise, you must have >= 3 number of $5 denominations
            elif fives > 3:
                fives -= 3
            # otherwise you can't give back the change, return False
            else:
                return False

    # finally, if all the customers can be given their change, return True.
    return True


print(is_change_possible([5, 5, 5, 10, 20]))
print(is_change_possible([5, 5, 10, 10, 20]))
